import json

from flask import Blueprint, Response

health_check_bp = Blueprint("healthcheck", __name__)


@health_check_bp.route("/health", methods=["GET"])
def check():
    # リクエストを受信
    return Response(
        response=json.dumps(
            {
                "isOK": True,
            }
        ),
        status=200,
    )
