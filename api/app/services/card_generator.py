import logging
import os
from io import BytesIO

import requests
from openai import OpenAI
from PIL import Image, ImageDraw, ImageFilter, ImageFont

from app.models.frame import Frame
from app.models.prompt_items import PromptItems
from app.models.prompt_levels import PromptLevels


class CardGenerator:
    def __init__(self, request):
        self.planet_name = request.get("planetName")
        self.prompt_items = PromptItems(
            diameter=request.get("diameter"),
            gravity=request.get("gravity"),
            distance=request.get("distance"),
            temperature=request.get("temperature"),
            atmosphere=request.get("atmosphere"),
            water=request.get("water"),
            terrain=request.get("terrain"),
            volcano=request.get("volcano"),
            aurora=request.get("aurora"),
        )
        self.prompt_items_level = self.calc_level()

    def calc_level(self):
        if 1000 <= self.prompt_items.diameter <= 20900:
            diameter_level = 1
        elif 20901 <= self.prompt_items.diameter <= 40800:
            diameter_level = 2
        elif 40801 <= self.prompt_items.diameter <= 60700:
            diameter_level = 3
        elif 60701 <= self.prompt_items.diameter <= 80600:
            diameter_level = 4
        elif 80601 <= self.prompt_items.diameter <= 100500:
            diameter_level = 5
        elif 100501 <= self.prompt_items.diameter <= 120400:
            diameter_level = 6
        elif 120401 <= self.prompt_items.diameter <= 140300:
            diameter_level = 7
        elif 140301 <= self.prompt_items.diameter <= 160200:
            diameter_level = 8
        elif 160201 <= self.prompt_items.diameter <= 180100:
            diameter_level = 9
        elif 180101 <= self.prompt_items.diameter <= 200000:
            diameter_level = 10
        else:
            diameter_level = None

        if 0.0 <= self.prompt_items.gravity <= 0.5:
            gravity_level = 1
        elif 0.51 <= self.prompt_items.gravity <= 1.0:
            gravity_level = 2
        elif 1.01 <= self.prompt_items.gravity <= 1.5:
            gravity_level = 3
        elif 1.51 <= self.prompt_items.gravity <= 2.0:
            gravity_level = 4
        elif 2.01 <= self.prompt_items.gravity <= 2.5:
            gravity_level = 5
        elif 2.51 <= self.prompt_items.gravity <= 3.0:
            gravity_level = 6
        elif 3.01 <= self.prompt_items.gravity <= 3.5:
            gravity_level = 7
        elif 3.51 <= self.prompt_items.gravity <= 4.0:
            gravity_level = 8
        elif 4.01 <= self.prompt_items.gravity <= 4.5:
            gravity_level = 9
        elif 4.51 <= self.prompt_items.gravity <= 5.0:
            gravity_level = 10
        else:
            gravity_level = None

        if 50 <= self.prompt_items.distance <= 545:
            distance_level = 1
        elif 546 <= self.prompt_items.distance <= 1040:
            distance_level = 2
        elif 1041 <= self.prompt_items.distance <= 1535:
            distance_level = 3
        elif 1536 <= self.prompt_items.distance <= 2030:
            distance_level = 4
        elif 2031 <= self.prompt_items.distance <= 2525:
            distance_level = 5
        elif 2526 <= self.prompt_items.distance <= 3020:
            distance_level = 6
        elif 3021 <= self.prompt_items.distance <= 3515:
            distance_level = 7
        elif 3516 <= self.prompt_items.distance <= 4010:
            distance_level = 8
        elif 4011 <= self.prompt_items.distance <= 4505:
            distance_level = 9
        elif 4506 <= self.prompt_items.distance <= 5000:
            distance_level = 10
        else:
            distance_level = None

        if -200 <= self.prompt_items.temperature <= -135:
            temperature_level = 1
        elif -134 <= self.prompt_items.temperature <= -100:
            temperature_level = 2
        elif -99 <= self.prompt_items.temperature <= -65:
            temperature_level = 3
        elif -64 <= self.prompt_items.temperature <= -30:
            temperature_level = 4
        elif -29 <= self.prompt_items.temperature <= 5:
            temperature_level = 5
        elif 6 <= self.prompt_items.temperature <= 40:
            temperature_level = 6
        elif 41 <= self.prompt_items.temperature <= 95:
            temperature_level = 7
        elif 96 <= self.prompt_items.temperature <= 150:
            temperature_level = 8
        elif 151 <= self.prompt_items.temperature <= 250:
            temperature_level = 9
        elif 251 <= self.prompt_items.temperature <= 500:
            temperature_level = 10
        else:
            temperature_level = None

        atmosphere_level = self.__calc_percent_level(self.prompt_items.atmosphere)
        water_level = self.__calc_percent_level(self.prompt_items.water)
        terrain_level = self.__calc_percent_level(self.prompt_items.terrain)
        volcano_level = self.__calc_percent_level(self.prompt_items.volcano)
        aurora_level = self.__calc_percent_level(self.prompt_items.aurora)

        return PromptLevels(
            diameter_level=diameter_level,
            gravity_level=gravity_level,
            distance_level=distance_level,
            temperature_level=temperature_level,
            atmosphere_level=atmosphere_level,
            water_level=water_level,
            terrain_level=terrain_level,
            volcano_level=volcano_level,
            aurora_level=aurora_level,
        )

    def __calc_percent_level(self, value):
        if 0 <= value <= 10:
            return 1
        elif 11 <= value <= 20:
            return 2
        elif 21 <= value <= 30:
            return 3
        elif 31 <= value <= 40:
            return 4
        elif 41 <= value <= 50:
            return 5
        elif 51 <= value <= 60:
            return 6
        elif 61 <= value <= 70:
            return 7
        elif 71 <= value <= 80:
            return 8
        elif 81 <= value <= 90:
            return 9
        elif 91 <= value <= 100:
            return 10
        else:
            return None

    def generate(self, prompt, save_path, image_id):
        try:
            result = OpenAI().images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1792",
                quality="standard",
                response_format="url",
            )
        except Exception as e:
            logging.error(f"ChatGPTの画像生成に失敗しました。: {e}", stack_info=True)
            return {
                "imageUrl": None,
                "imageId": None,
                "explanation": None,
                "rate": None,
                "code": "E01_001",
                "message": "ChatGPTの画像生成に失敗しました。",
            }

        try:
            # OpenAIによる画像の生成
            image_response = requests.get(result.data[0].url)
            ai_image = (
                Image.open(BytesIO(image_response.content)).convert("RGBA").copy()
            )

            # フレーム画像の選定
            frame = Frame.select_frame()

            # フレーム画像のファイルの読み込み
            frame_file_name = frame.get_file_name()
            frame_file_path = os.path.join(
                os.path.dirname(__file__),
                "..",
                "static",
                "template",
                "frame",
                frame_file_name,
            )
            frame_image = Image.open(frame_file_path).convert("RGBA")

            # フレーム画像をAI生成画像の横幅に一致するようにアスペクト比を保ったままリサイズ
            # MEMO: フレーム画像の方が大きい前提
            ai_image_width, ai_image_height = ai_image.size
            frame_image_width, frame_image_height = frame_image.size
            resized_frame_image_height = int(
                frame_image_height * (ai_image_width / frame_image_width)
            )
            resized_frame_image = frame_image.resize(
                (ai_image_width, resized_frame_image_height), Image.Resampling.LANCZOS
            )

            # 縦方向中央の位置を計算
            position = (0, abs(ai_image_height - resized_frame_image_height) // 2)

            # AI生成画像とフレーム画像の合成
            ai_image.paste(resized_frame_image, position, resized_frame_image)

            # 文字の合成
            base_font_file_path = os.path.join(
                os.path.dirname(__file__),
                "..",
                "static",
                "template",
                "font",
            )

            # 惑星名のシャドー合成
            name_x = 105
            name_y = 1350
            name_font_file_path = os.path.join(
                base_font_file_path,
                "KaKuDaron.TTF",
            )

            # シャドーの合成
            if len(self.planet_name) < 8:
                size = 100
            else:
                # 8文字以上の場合はフォントサイズを小さめにする。
                size = 86
                name_y += 10
            name_image_font = ImageFont.truetype(name_font_file_path, size=size)
            text_bbox = name_image_font.getbbox(self.planet_name)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]

            shadow_layer = Image.new("RGBA", ai_image.size, (0, 0, 0, 0))
            shadow_draw = ImageDraw.Draw(shadow_layer)
            padding = 24
            box = (
                name_x - padding,
                name_y - padding,
                name_x + text_width + padding,
                name_y + text_height + padding,
            )
            shadow_draw.rounded_rectangle(box, fill=frame.get_shadow_color(), radius=36)
            blurred_shadow = shadow_layer.filter(ImageFilter.GaussianBlur(radius=16))
            ai_image.alpha_composite(blurred_shadow)

            # 惑星名の合成
            output_image_draw = ImageDraw.Draw(ai_image)
            output_image_draw.text(
                (name_x, name_y),
                self.planet_name,
                font=name_image_font,
                fill=(255, 255, 255, 255),
            )

            # パラメータの合成
            param_text = f"diameter:{self.prompt_items.diameter}, gravity:{self.prompt_items.gravity}, distance:{self.prompt_items.distance}, temperature:{self.prompt_items.temperature}, \natmosphere:{self.prompt_items.atmosphere}, water:{self.prompt_items.water}, terrain:{self.prompt_items.terrain}, volcano:{self.prompt_items.volcano}, aurora:{self.prompt_items.aurora}\n"
            param_font_file_path = os.path.join(
                base_font_file_path,
                "NotoSansJP.ttf",
            )
            output_image_draw.text(
                (280, 1550),
                param_text,
                font=ImageFont.truetype(param_font_file_path, size=21),
                fill=(255, 255, 255, 255),
            )

            # 印刷用の画像のクロップ
            trim_x_px = 110.93
            output_image = ai_image.crop(
                (0, trim_x_px, ai_image_width, ai_image_height - trim_x_px)
            )

            # 印刷用の画像の保存
            output_image.save(os.path.join(save_path, f"{image_id}.png"))

            # フロント表示用の画像のクロップ
            trim_x_px = 51.20
            trim_y_px = 162.13
            output_display_image = ai_image.crop(
                (
                    trim_x_px,
                    trim_y_px,
                    ai_image_width - trim_x_px,
                    ai_image_height - trim_y_px,
                )
            )

            # 画像の保存
            output_image_file_name = f"{image_id}_display.png"
            output_display_image.save(os.path.join(save_path, output_image_file_name))

            # テキスト(パラメータ)の保存
            with open(os.path.join(save_path, f"{image_id}.txt"), mode="w") as f:
                f.write(param_text)

            return {
                "imageFileName": output_image_file_name,
                "imageUrl": None,
                "imageId": None,
                "explanation": None,
                "rate": None,
                "code": None,
                "message": None,
            }
        except FileNotFoundError as fnfe:
            logging.error(
                f"ファイル、もしくはディレクトリが存在しません。: {fnfe}",
                stack_info=True,
            )
            return {
                "imageFileName": None,
                "imageUrl": None,
                "imageId": None,
                "explanation": None,
                "rate": None,
                "code": "E01_002",
                "message": "ファイル、もしくはディレクトリが存在しません。",
            }
        except FileExistsError as fee:
            logging.error(f"ファイルが既に存在します。: {fee}", stack_info=True)
            return {
                "imageFileName": None,
                "imageUrl": None,
                "imageId": None,
                "explanation": None,
                "rate": None,
                "code": "E01_003",
                "message": "ファイルが既に存在します。",
            }
        except PermissionError as pe:
            logging.error(
                f"ファイルへのアクセス権限がありません。: {pe}", stack_info=True
            )
            return {
                "imageFileName": None,
                "imageUrl": None,
                "imageId": None,
                "explanation": None,
                "rate": None,
                "code": "E01_004",
                "message": "ファイルへのアクセス権限がありません。",
            }
        except IOError as ioe:
            logging.error(
                f"ファイル操作でエラーが発生しました。: {ioe}", stack_info=True
            )
            return {
                "imageFileName": None,
                "imageUrl": None,
                "imageId": None,
                "explanation": None,
                "rate": None,
                "code": "E01_005",
                "message": "ファイル操作でエラーが発生しました。",
            }
