import textwrap

from app.models.prompt_define import PromptDefine


class PromptBuilder:
    def __init__(self, planet_name, prompt_levels):
        self.planet_name = planet_name
        self.levels = prompt_levels

    def build_ai_image_prompt(self):
        # prompt_levels.xxx_levelは1オリジンのため、-1をしてリストのインデックスに合うように調整
        return f"{PromptDefine.DIAMETER.value[self.levels.diameter_level - 1]}, {PromptDefine.GRAVITY.value[self.levels.gravity_level - 1]}, {PromptDefine.DISTANCE.value[self.levels.distance_level - 1]}. The planet has {PromptDefine.TEMPERATURE.value[self.levels.temperature_level - 1]} and {PromptDefine.ATMOSPHERE.value[self.levels.atmosphere_level - 1]}. Its surface is {PromptDefine.WATER.value[self.levels.water_level - 1]}, {PromptDefine.TERRAIN.value[self.levels.terrain_level - 1]}, {PromptDefine.VOLCANO.value[self.levels.volcano_level - 1]}, and {PromptDefine.AURORA.value[self.levels.aurora_level - 1]}. The planet is shown floating in deep black space with distant stars, lit from one side to create depth and shadow. Style: NASA-like high-quality space illustration."

    def build_description_prompt(self):
        # prompt_levels.xxx_levelは1オリジンのため、-1をしてリストのインデックスに合うように調整
        return textwrap.dedent(
            f"""
            あなたは子ども向けの宇宙図鑑を作る専門家です。次の情報を元に惑星「{self.planet_name}」の小学生向け図鑑風紹介文を170文字程度で書いてください。この惑星の名前「{self.planet_name}」から想像できる雰囲気やイメージを少しだけ紹介文に取り入れてください。名前は文の最初に紹介してください。
            diameter: {PromptDefine.DIAMETER.value[self.levels.diameter_level - 1]}
            gravity: {PromptDefine.GRAVITY.value[self.levels.gravity_level - 1]}
            distance: {PromptDefine.DISTANCE.value[self.levels.distance_level - 1]}
            temperature: {PromptDefine.TEMPERATURE.value[self.levels.temperature_level - 1]}
            atmosphere: {PromptDefine.ATMOSPHERE.value[self.levels.atmosphere_level - 1]}
            water: {PromptDefine.WATER.value[self.levels.water_level - 1]}
            terrain: {PromptDefine.TERRAIN.value[self.levels.terrain_level - 1]}
            volcano: {PromptDefine.VOLCANO.value[self.levels.volcano_level - 1]}
            aurora: {PromptDefine.AURORA.value[self.levels.aurora_level - 1]}
       """
        ).strip()
