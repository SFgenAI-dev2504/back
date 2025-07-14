import json
import logging
import os
import random
from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Blueprint, current_app, jsonify, request

from app.services.card_generator_service import CardGeneratorService
from app.services.prompt_creator_service import PromptCreatorService

generate_bp = Blueprint("generate", __name__)


@generate_bp.route("/generate", methods=["POST"])
def generate():
    # リクエストを受信
    req = request.get_json()
    planet_name = req.get("planetName")
    logging.info("リクエスト: " + json.dumps(req, ensure_ascii=False))

    cardGeneratorService = CardGeneratorService(req)
    logging.info(cardGeneratorService.prompt_items_level)

    promptCreatorService = PromptCreatorService(cardGeneratorService.prompt_items_level)

    # プロンプトの生成
    prompt = promptCreatorService.create(current_app.config.get("OPENAI_API_KEY"))

    # 画像ID=アウトプットのベースディレクトリの作成(yyyymmddhhmmss_xxxx)
    jst_time = datetime.now(ZoneInfo("Asia/Tokyo"))
    timestamp = jst_time.strftime("%Y%m%d%H%M%S")
    image_id = f"{timestamp}_{random.randint(1000, 9999)}"
    save_path = os.path.join(
        os.path.dirname(__file__), "..", "static", "output", image_id
    )
    os.makedirs(save_path, exist_ok=True)

    # OpenAIによる画像の生成
    output_ai_image_file_name = cardGeneratorService.generate(
        prompt, save_path, image_id
    )

    # フロントに返却
    output_static_base_path = current_app.config.get("SERVER_IMAGE_PATH")
    imageUrl = os.path.join(
        output_static_base_path, image_id, output_ai_image_file_name
    )
    return jsonify({"imageUrl": imageUrl, "imageId": image_id})
