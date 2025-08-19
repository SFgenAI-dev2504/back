import json
import logging
import os

from flask import Blueprint, Response, current_app, request

from app.services.card_desicion import CardDecision

decide_bp = Blueprint("decide", __name__)


@decide_bp.route("/decide", methods=["POST"])
def decide():
    # リクエストを受信
    req = request.get_json()
    image_id = req.get("imageId")
    logging.info("リクエスト: " + json.dumps(req, ensure_ascii=False))

    submit_file_name = current_app.config.get("SERVER_SUBMIT_FILE_NAME")
    card_decision = CardDecision(image_id, submit_file_name)
    save_path = os.path.join(os.path.dirname(__file__), "..", "static", "output")

    try:
        # submitファイルの作成
        body = card_decision.decide(save_path)
        if body.get("code") is None and body.get("message") is None:
            return Response(response=json.dumps(body), status=200)
        else:
            return Response(response=json.dumps(body), status=500)
    except Exception as e:
        logging.error(
            f"${submit_file_name}ファイルのファイル操作で予期せぬエラーが発生しました。: {e}",
            stack_info=True,
        )
        return Response(
            response=json.dumps(
                {
                    "code": "E02_005",
                    "message": f"${submit_file_name}ファイルのファイル操作で予期せぬエラーが発生しました。",
                }
            ),
            status=500,
        )
