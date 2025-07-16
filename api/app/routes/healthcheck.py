import json
import logging
import os

from flask import Blueprint, Response, current_app, request

from app.services.decision_service import DecisionService

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
