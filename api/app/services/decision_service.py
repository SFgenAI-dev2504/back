import logging
import os


class DecisionService:
    def __init__(self, request):
        self.image_id = request.get("imageId")

    def decide(self, save_path):
        # 書き込みファイルパスの生成
        submit_file_path = os.path.join(save_path, "submit.txt")

        # ファイル書き込み(新規作成 or 追記)
        try:
            with open(submit_file_path, "a", encoding="utf-8") as f:
                f.write(f"・画像ID：{self.image_id}\n")
            return {"isOK": True}
        except FileNotFoundError as fnfe:
            logging.error(
                f"submitファイル、もしくはディレクトリが存在しません。: {fnfe}"
            )
            return {
                "isOK": False,
                "code": "E02_001",
                "message": "submitファイル、もしくはディレクトリが存在しません。",
            }
        except FileExistsError as fee:
            logging.error(f"submitファイルが既に存在します。: {fee}")
            return {
                "isOK": False,
                "code": "E02_002",
                "message": "submitファイルが既に存在します。",
            }
        except PermissionError as pe:
            logging.error(f"submitファイルへのアクセス権限がありません。: {pe}")
            return {
                "isOK": False,
                "code": "E02_003",
                "message": "submitファイルへのアクセス権限がありません。",
            }
        except IOError as ioe:
            logging.error(
                f"submitファイルのファイル操作でエラーが発生しました。: {ioe}"
            )
            return {
                "isOK": False,
                "code": "E02_004",
                "message": "submitファイルのファイル操作でエラーが発生しました。",
            }
        except Exception as e:
            raise e
