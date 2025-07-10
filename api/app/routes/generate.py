import json
import logging
import os
from datetime import datetime

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
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_base_dir = f"sam_{timestamp}_{planet_name}"
    save_path = os.path.join(
        os.path.dirname(__file__), "..", "static", "images", output_base_dir
    )
    os.makedirs(save_path, exist_ok=True)

    # OpenAIによる画像の生成
    output_base_path = current_app.config.get("SERVER_IMAGE_PATH")
    output_ai_image_file_name = cardGeneratorService.generate(prompt, output_base_dir)
    ai_image_file_path = os.path.join(output_base_path, output_ai_image_file_name)

    # PPTXを元に画像の加工
    pptx_path = current_app.config.get("SERVER_PPTX_PATH")
    pptxOperatorService = PPTXOperatorService(pptx_path, output_base_path)
    output_image_file_name = pptxOperatorService.create_image(ai_image_file_path)
    return jsonify({"imageUrl": f"{output_base_path}/{output_image_file_name}"})
