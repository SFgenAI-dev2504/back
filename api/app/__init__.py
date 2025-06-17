import logging
import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from .models.db import init_db
from .routes.generate import index_bp


def create_app():
    # .envファイルを読み込み
    load_dotenv()

    # appの設定
    app = Flask(__name__)
    CORS(app)

    app.config["API_KEY"] = os.environ.get("API_KEY")
    app.config["DB_HOST"] = os.environ.get("DB_HOST")
    app.config["DB_USER"] = os.environ.get("DB_USER")
    app.config["DB_PASSWORD"] = os.environ.get("DB_PASSWORD")
    app.config["DB_NAME"] = os.environ.get("DB_NAME")

    # DBの設定
    init_db(app)

    # Blueprintの設定
    app.register_blueprint(index_bp)

    # ログの設定
    logging.basicConfig(level=logging.DEBUG)

    return app
