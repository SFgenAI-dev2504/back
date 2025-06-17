import logging

from flask import Blueprint, current_app, jsonify, request

from app.services.card_generator_service import CardGeneratorService
from app.services.prompt_creator_service import PromptCreatorService

index_bp = Blueprint("index", __name__)


@index_bp.route("/generate", methods=["GET", "POST"])
def generate():
    req = request.get_json()
    logging.info("リクエスト: " + req)
    api_key = current_app.config.get("OPENAI_API_KEY")

    cardGeneratorService = CardGeneratorService(req)
    promptCreatorService = PromptCreatorService(cardGeneratorService.prompt_items_level)
    prompt = promptCreatorService.create(api_key)

    file_name = cardGeneratorService.generate(prompt)

    result = {"imageUrl": "http://localhost:5001/static/images/" + file_name}
    return jsonify(result)
