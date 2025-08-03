import logging
import os


class DecisionService:
    def __init__(self, image_id, file_name):
        self.image_id = image_id
        self.file_name = file_name

    def decide(self, save_path):
        # 書き込みファイルパスの生成
        submit_file_path = os.path.join(save_path, self.file_name)

        try:
            if os.path.exists(submit_file_path):
                # 同じimage_idが書き込まれている場合はエラーを返す
                with open(submit_file_path, "r", encoding="utf-8") as f:
                    logging.info(self.image_id)
                    for line in f:
                        if self.image_id in line:
                            logging.error(
                                f"{self.file_name}ファイルに重複した画像IDが存在します。",
                                stack_info=True,
                            )
                            return {
                                "code": "E02_006",
                                "message": f"{self.file_name}ファイルに重複した画像IDが存在します。",
                            }

            # ファイル書き込み(新規作成 or 追記)
            with open(submit_file_path, "a", encoding="utf-8") as f:
                f.write(f"・画像ID：{self.image_id}\n")
            return {"code": None, "message": None}
        except FileNotFoundError as fnfe:
            logging.error(
                f"{self.file_name}ファイル、もしくはディレクトリが存在しません。: {fnfe}",
                stack_info=True,
            )
            return {
                "code": "E02_001",
                "message": f"{self.file_name}ファイル、もしくはディレクトリが存在しません。",
            }
        except FileExistsError as fee:
            logging.error(
                f"{self.file_name}ファイルが既に存在します。: {fee}", stack_info=True
            )
            return {
                "code": "E02_002",
                "message": f"{self.file_name}ファイルが既に存在します。",
            }
        except PermissionError as pe:
            logging.error(
                f"{self.file_name}ファイルへのアクセス権限がありません。: {pe}",
                stack_info=True,
            )
            return {
                "code": "E02_003",
                "message": f"{self.file_name}ファイルへのアクセス権限がありません。",
            }
        except IOError as ioe:
            logging.error(
                f"{self.file_name}ファイルのファイル操作でエラーが発生しました。: {ioe}",
                stack_info=True,
            )
            return {
                "code": "E02_004",
                "message": f"{self.file_name}ファイルのファイル操作でエラーが発生しました。",
            }
        except Exception as e:
            raise e
