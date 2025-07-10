import json
import logging
import os
from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Blueprint, current_app, jsonify, request

from app.services.card_generator_service import CardGeneratorService
from app.services.pptx_operator_service import PPTXOperatorService
from app.services.prompt_creator_service import PromptCreatorService

index_bp = Blueprint("index", __name__)


@index_bp.route("/generate", methods=["GET", "POST"])
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

    # アウトプットのベースディレクトリの作成
    jst_time = datetime.now(ZoneInfo("Asia/Tokyo"))
    timestamp = jst_time.strftime("%Y%m%d%H%M%S")
    output_base_path = f"sam_{timestamp}_{planet_name}"
    save_path = os.path.join(
        os.path.dirname(__file__), "..", "static", "images", output_base_path
    )
    os.makedirs(save_path, exist_ok=True)

    # OpenAIによる画像の生成
    output_ai_image_file_name = cardGeneratorService.generate(prompt, save_path)

    # PPTXを元に画像の加工
    pptx_file_name = current_app.config.get("SERVER_ORIGINAL_PPTX_FILE_NAME")
    # pptxOperatorService = PPTXOperatorService(pptx_file_name, save_path)
    # pptxOperatorService.insert_image(output_ai_image_file_name)
    # pptxOperatorService.export_image()

    # 画像ファイルのパスをフロントに返却
    output_static_base_path = current_app.config.get("SERVER_IMAGE_PATH")
    imageUrl = os.path.join(
        output_static_base_path, output_base_path, output_ai_image_file_name
    )
    return jsonify({"imageUrl": imageUrl})
