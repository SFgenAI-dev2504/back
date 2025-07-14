import json
import logging
import os

from flask import Blueprint, request

from app.services.decision_service import DecisionService

decide_bp = Blueprint("decide", __name__)


@decide_bp.route("/decide", methods=["POST"])
def decide():
    # リクエストを受信
    req = request.get_json()
    image_id = req.get("imageId")
    logging.info("リクエスト: " + json.dumps(req, ensure_ascii=False))

    decision_service = DecisionService(req)
    save_path = os.path.join(
        os.path.dirname(__file__), "..", "static", "output", image_id
    )

    # submitファイルの作成
    try:
        return decision_service.decide(save_path)
    except Exception as e:
        logging.error(
            f"submitファイルのファイル操作で予期せぬエラーが発生しました。: {e}"
        )
        return {
            "isOK": False,
            "code": "E02_005",
            "message": "submitファイルのファイル操作で予期せぬエラーが発生しました。",
        }
