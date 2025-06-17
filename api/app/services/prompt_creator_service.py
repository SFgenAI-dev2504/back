import logging

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


class PromptCreatorService:
    def __init__(self, level):
        self.prompt_items_level = level
        self.system_prompt = """\
            あなたはAIに関する経験が豊富な、優秀なプロンプトエンジニアです。 \
            以下の「プロンプト作成のルール」に従って、\
            DALL-E3に効果的な指示を与えるためのプロンプトを考えてください。
            
            ***プロンプト作成のルール***
            具体的で明確な表現をすること
            ユーザーの入力に基づいて、繊細で想像力豊かな画像を作成すること
            ビジュアルが鮮明になるよう色・形・動き・状況などを具体的に記述すること
            指示された内容自体は含まないこと
            \
            """

    def create(self, api_key):
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.system_prompt),
                ("human", "{input}"),
            ]
        )
        model = ChatOpenAI(model="gpt-4o", temperature=0.5, api_key=api_key)

        chain = prompt | model | StrOutputParser()
        return chain.invoke({"input": self.__create_all_prompt()})

    def __create_all_prompt(self):
        text = ""
        text += self.__create_diameter_prompt()
        text += self.__create_gravity_prompt()
        text += self.__create_distance_prompt()
        text += self.__create_temperature_prompt()
        text += self.__create_atmosphere_prompt()
        text += self.__create_water_prompt()
        text += self.__create_terrain_prompt()
        text += self.__create_volcano_prompt()
        text += self.__create_aurora_prompt()
        text += "The planet is shown floating in deep black space with distant stars, lit from one side to create depth and shadow. Style: NASA-like high-quality space illustration."
        logging.info("プロンプト: " + text)
        return text

    def __create_diameter_prompt(self):
        prompt = ""
        if self.prompt_items_level.diameter_level == 1:
            prompt = "A tiny planet"
        elif self.prompt_items_level.diameter_level == 2:
            prompt = "A very small planet"
        elif self.prompt_items_level.diameter_level == 3:
            prompt = "A small planet"
        elif self.prompt_items_level.diameter_level == 4:
            prompt = "A medium-small planet"
        elif self.prompt_items_level.diameter_level == 5:
            prompt = "A medium-sized planet"
        elif self.prompt_items_level.diameter_level == 6:
            prompt = "A medium-large planet"
        elif self.prompt_items_level.diameter_level == 7:
            prompt = "A large planet"
        elif self.prompt_items_level.diameter_level == 8:
            prompt = "A very large planet"
        elif self.prompt_items_level.diameter_level == 9:
            prompt = "A huge planet"
        elif self.prompt_items_level.diameter_level == 10:
            prompt = "A gigantic planet"
        return prompt + " "

    def __create_gravity_prompt(self):
        prompt = ""
        if self.prompt_items_level.gravity_level == 1:
            prompt = "with microgravity"
        elif self.prompt_items_level.gravity_level == 2:
            prompt = "with low gravity"
        elif self.prompt_items_level.gravity_level == 3:
            prompt = "with Earth-like gravity"
        elif self.prompt_items_level.gravity_level == 4:
            prompt = "with slightly strong gravity"
        elif self.prompt_items_level.gravity_level == 5:
            prompt = "with strong gravity"
        elif self.prompt_items_level.gravity_level == 6:
            prompt = "with heavy gravity"
        elif self.prompt_items_level.gravity_level == 7:
            prompt = "with very strong gravity"
        elif self.prompt_items_level.gravity_level == 8:
            prompt = "with crushing gravity"
        elif self.prompt_items_level.gravity_level == 9:
            prompt = "with extreme gravity"
        elif self.prompt_items_level.gravity_level == 10:
            prompt = "with impossible gravity"
        return prompt + ", "

    def __create_distance_prompt(self):
        prompt = ""
        if self.prompt_items_level.distance_level == 1:
            prompt = "orbiting very close to its star"
        elif self.prompt_items_level.distance_level == 2:
            prompt = "orbiting close to its star"
        elif self.prompt_items_level.distance_level == 3:
            prompt = "orbiting at a warm distance"
        elif self.prompt_items_level.distance_level == 4:
            prompt = "orbiting moderately far from its star"
        elif self.prompt_items_level.distance_level == 5:
            prompt = "orbiting far from its star"
        elif self.prompt_items_level.distance_level == 6:
            prompt = "orbiting at a cold distance"
        elif self.prompt_items_level.distance_level == 7:
            prompt = "orbiting very far from its star"
        elif self.prompt_items_level.distance_level == 8:
            prompt = "orbiting in deep space"
        elif self.prompt_items_level.distance_level == 9:
            prompt = "orbiting extremely far from its star"
        elif self.prompt_items_level.distance_level == 10:
            prompt = "orbiting at the edge of a solar system"
        return prompt + ". "

    def __create_temperature_prompt(self):
        prompt = ""
        if self.prompt_items_level.temperature_level == 1:
            prompt = "with a deeply frozen surface"
        elif self.prompt_items_level.temperature_level == 2:
            prompt = "with a frigid surface"
        elif self.prompt_items_level.temperature_level == 3:
            prompt = "with an icy landscape"
        elif self.prompt_items_level.temperature_level == 4:
            prompt = "with a cold environment"
        elif self.prompt_items_level.temperature_level == 5:
            prompt = "with a chilly climate"
        elif self.prompt_items_level.temperature_level == 6:
            prompt = "with a temperate climate"
        elif self.prompt_items_level.temperature_level == 7:
            prompt = "with a warm, dry surface"
        elif self.prompt_items_level.temperature_level == 8:
            prompt = "with a hot surface"
        elif self.prompt_items_level.temperature_level == 9:
            prompt = "with an extremely hot surface"
        elif self.prompt_items_level.temperature_level == 10:
            prompt = "with a scorched, volcanic surface"
        return "The planet has" + prompt + " and "

    def __create_atmosphere_prompt(self):
        prompt = ""
        if self.prompt_items_level.atmosphere_level == 1:
            prompt = "with no atmosphere, exposing the bare surface"
        elif self.prompt_items_level.atmosphere_level == 2:
            prompt = "with a whisper-thin atmosphere"
        elif self.prompt_items_level.atmosphere_level == 3:
            prompt = "with a thin, dusty atmosphere"
        elif self.prompt_items_level.atmosphere_level == 4:
            prompt = "with a light atmosphere and wispy clouds"
        elif self.prompt_items_level.atmosphere_level == 5:
            prompt = "with a moderate atmosphere and some clouds"
        elif self.prompt_items_level.atmosphere_level == 6:
            prompt = "with a thicker atmosphere and noticeable haze"
        elif self.prompt_items_level.atmosphere_level == 7:
            prompt = "with a dense atmosphere and swirling winds"
        elif self.prompt_items_level.atmosphere_level == 8:
            prompt = "with a heavy atmosphere and frequent storms"
        elif self.prompt_items_level.atmosphere_level == 9:
            prompt = "with an extremely thick atmosphere"
        elif self.prompt_items_level.atmosphere_level == 10:
            prompt = "with a suffocating atmosphere of dense gases"
        return prompt + ". "

    def __create_water_prompt(self):
        prompt = ""
        if self.prompt_items_level.water_level == 1:
            prompt = "completely dry, with no visible water"
        elif self.prompt_items_level.water_level == 2:
            prompt = "with a few small puddles or dried riverbeds"
        elif self.prompt_items_level.water_level == 3:
            prompt = "with occasional streams or isolated lakes"
        elif self.prompt_items_level.water_level == 4:
            prompt = "with scattered lakes and small rivers"
        elif self.prompt_items_level.water_level == 5:
            prompt = "with rivers and modest seas"
        elif self.prompt_items_level.water_level == 6:
            prompt = "with half the surface covered in water"
        elif self.prompt_items_level.water_level == 7:
            prompt = "with large seas and small oceans"
        elif self.prompt_items_level.water_level == 8:
            prompt = "mostly covered in water with vast oceans"
        elif self.prompt_items_level.water_level == 9:
            prompt = "nearly submerged with only small landmasses visible"
        elif self.prompt_items_level.water_level == 10:
            prompt = "entirely ocean-covered, like a water world"
        return "Its surface is " + prompt + ", "

    def __create_terrain_prompt(self):
        prompt = ""
        if self.prompt_items_level.terrain_level == 1:
            prompt = "with a perfectly smooth and flat surface"
        elif self.prompt_items_level.terrain_level == 2:
            prompt = "with gentle rolling plains"
        elif self.prompt_items_level.terrain_level == 3:
            prompt = "with small hills and light undulations"
        elif self.prompt_items_level.terrain_level == 4:
            prompt = "with minor craters and ridges"
        elif self.prompt_items_level.terrain_level == 5:
            prompt = "with a balanced mix of hills, plains, and shallow valleys"
        elif self.prompt_items_level.terrain_level == 6:
            prompt = "with noticeable elevation changes and rock formations"
        elif self.prompt_items_level.terrain_level == 7:
            prompt = "with rugged terrain and scattered mountains"
        elif self.prompt_items_level.terrain_level == 8:
            prompt = "with steep cliffs and large craters"
        elif self.prompt_items_level.terrain_level == 9:
            prompt = "with chaotic, heavily cratered landscapes"
        elif self.prompt_items_level.terrain_level == 10:
            prompt = "with extreme topography, sharp ridges and deep canyons"
        return prompt + ", "

    def __create_volcano_prompt(self):
        prompt = ""
        if self.prompt_items_level.volcano_level == 1:
            prompt = "with no signs of volcanic activity"
        elif self.prompt_items_level.volcano_level == 2:
            prompt = "with extinct volcanoes and hardened lava fields"
        elif self.prompt_items_level.volcano_level == 3:
            prompt = "with occasional dormant volcanoes"
        elif self.prompt_items_level.volcano_level == 4:
            prompt = "with scattered inactive volcanoes"
        elif self.prompt_items_level.volcano_level == 5:
            prompt = "with signs of minor volcanic activity"
        elif self.prompt_items_level.volcano_level == 6:
            prompt = "with a few active volcanoes emitting smoke"
        elif self.prompt_items_level.volcano_level == 7:
            prompt = "with frequent volcanic eruptions"
        elif self.prompt_items_level.volcano_level == 8:
            prompt = "with lava rivers and glowing craters"
        elif self.prompt_items_level.volcano_level == 9:
            prompt = "with major volcanic zones and widespread eruptions"
        elif self.prompt_items_level.volcano_level == 10:
            prompt = "with extreme volcanic activity and a molten landscape"
        return prompt + ", and "

    def __create_aurora_prompt(self):
        prompt = ""
        if self.prompt_items_level.aurora_level == 1:
            prompt = "with no auroras visible in the sky"
        elif self.prompt_items_level.aurora_level == 2:
            prompt = "with rare, faint auroras near the poles"
        elif self.prompt_items_level.aurora_level == 3:
            prompt = "with occasional auroras in polar regions"
        elif self.prompt_items_level.aurora_level == 4:
            prompt = "with gentle aurora glow appearing at night"
        elif self.prompt_items_level.aurora_level == 5:
            prompt = "with auroras shimmering faintly across the skies"
        elif self.prompt_items_level.aurora_level == 6:
            prompt = "with clearly visible auroras in motion"
        elif self.prompt_items_level.aurora_level == 7:
            prompt = "with colorful auroras stretching across the horizon"
        elif self.prompt_items_level.aurora_level == 8:
            prompt = "with vivid auroras swirling above the surface"
        elif self.prompt_items_level.aurora_level == 9:
            prompt = "with brilliant auroras illuminating the sky"
        elif self.prompt_items_level.aurora_level == 10:
            prompt = "with spectacular auroras dancing in all directions"
        return prompt + ". "
