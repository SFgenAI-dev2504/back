import json
import logging
import os
import random
from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Blueprint, Response, current_app, request

from app.infrastructure.chat_gpt_client import ChatGPTClient
from app.services.card_generator_service import CardGeneratorService
from app.services.prompt_builder import PromptBuilder

generate_bp = Blueprint("generate", __name__)


@generate_bp.route("/generate", methods=["POST"])
def generate():
    # リクエストを受信
    req = request.get_json()
    logging.info("リクエスト: " + json.dumps(req, ensure_ascii=False))

    # リクエスト値からレベルの計算
    cardGeneratorService = CardGeneratorService(req)
    levels = cardGeneratorService.prompt_items_level
    logging.info(levels)

    # プロンプトの生成
    promptBuilder = PromptBuilder(req.get("planetName"), levels)
    chatGPTClient = ChatGPTClient(
        current_app.config.get("OPENAI_API_KEY"), promptBuilder
    )
    answer_ai_image_prompt = chatGPTClient.ask_ai_image_prompt()
    answer_description_prompt = chatGPTClient.ask_description_prompt()

    # 画像ID=アウトプットのベースディレクトリの作成(yyyymmddhhmmss_xxxx)
    jst_time = datetime.now(ZoneInfo("Asia/Tokyo"))
    timestamp = jst_time.strftime("%Y%m%d%H%M%S")
    image_id = f"{timestamp}_{random.randint(1000, 9999)}"
    save_path = os.path.join(
        os.path.dirname(__file__), "..", "static", "output", image_id
    )
    os.makedirs(save_path, exist_ok=True)

    # OpenAIによる画像の生成
    try:
        body = cardGeneratorService.generate(
            answer_ai_image_prompt, save_path, image_id
        )
        logging.info(body)
        image_file_name = body.get("imageFileName")

        if body.get("code") is None and body.get("message") is None:
            output_static_base_path = current_app.config.get("SERVER_IMAGE_PATH")
            return Response(
                response=json.dumps(
                    {
                        "imageFileName": image_file_name,
                        "imageUrl": os.path.join(
                            output_static_base_path, image_id, image_file_name
                        ),
                        "imageId": image_id,
                        "explanation": answer_description_prompt,
                        "rate": 1,
                        "code": None,
                        "message": None,
                    }
                ),
                status=200,
            )
        else:
            return Response(response=json.dumps(body), status=500)
    except Exception as e:
        logging.error(f"画像生成で予期せぬエラーが発生しました。: {e}", stack_info=True)
        return Response(
            response=json.dumps(
                {
                    "imageFileName": None,
                    "imageUrl": None,
                    "imageId": None,
                    "explanation": None,
                    "rate": None,
                    "code": "E01_006",
                    "message": "画像生成で予期せぬエラーが発生しました。",
                }
            ),
            status=500,
        )
