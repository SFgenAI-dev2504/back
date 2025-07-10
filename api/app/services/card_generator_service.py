import logging
import os
import random
from datetime import datetime
from io import BytesIO

import requests
from openai import OpenAI
from PIL import Image

from app.models.prompt_items import PromptItems
from app.models.prompt_levels import PromptLevels


class CardGeneratorService:
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

    def generate(self, prompt, output_base_path):
        result = OpenAI().images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            response_format="url",
            style="natural",
        )

        # OpenAIによる画像の生成
        image_response = requests.get(result.data[0].url)
        image = Image.open(BytesIO(image_response.content)).convert("RGBA")

        # 画像の保存
        output_image_file_name = "output.png"
        image.save(os.path.join(output_base_path, output_image_file_name))

        # テキスト(パラメータ)の保存
        param_text = f"name: {self.planet_name}, diameter:{self.prompt_items.diameter}, gravity:{self.prompt_items.gravity}, distance:{self.prompt_items.distance}, temperature:{self.prompt_items.temperature}, atmosphere:{self.prompt_items.atmosphere}, water:{self.prompt_items.water}, terrain:{self.prompt_items.terrain}, volcano:{self.prompt_items.volcano}, aurora :{self.prompt_items.aurora}\n"
        with open(os.path.join(output_base_path, "output.txt"), mode="w") as f:
            f.write(param_text)

        return output_image_file_name
