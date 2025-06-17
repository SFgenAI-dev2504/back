import logging

from flask import Blueprint, current_app, jsonify, request

from app.services.card_generator_service import CardGeneratorService
from app.services.prompt_creator_service import PromptCreatorService

index_bp = Blueprint("index", __name__)


@index_bp.route("/generate", methods=["GET", "POST"])
def generate():
    # リクエストを受信
    req = request.get_json()
    logging.info("リクエスト: " + req)

    cardGeneratorService = CardGeneratorService(req)
    promptCreatorService = PromptCreatorService(cardGeneratorService.prompt_items_level)

    # プロンプトの生成
    prompt = promptCreatorService.create(current_app.config.get("OPENAI_API_KEY"))

    # 画像の生成
    file_name = cardGeneratorService.generate(prompt)

    result = {"imageUrl": "http://localhost:5001/static/images/" + file_name}
    return jsonify(result)
