import logging

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


class ChatGPTClient:
    def __init__(self, api_key, prompt_builder):
        self.api_key = api_key
        self.prompt_builder = prompt_builder
        self.chain = self.__build_chain()

    def __build_chain(self):
        system_prompt = """\
            あなたはAIに関する経験が豊富な、優秀なプロンプトエンジニアです。 \
            以下の「プロンプト作成のルール」に従って、DALL-E3に効果的な指示を与えるためのプロンプトを考えてください。
            
            ***プロンプト作成のルール***
            具体的で明確な表現をすること
            ユーザーの入力に基づいて、繊細で想像力豊かな画像を作成すること
            ビジュアルが鮮明になるよう色・形・動き・状況などを具体的に記述すること
            指示された内容自体は含まないこと
            """
        prompt = ChatPromptTemplate.from_messages(
            [("system", system_prompt), ("human", "{input}")]
        )
        model = ChatOpenAI(model="gpt-4o", temperature=0.5, api_key=self.api_key)
        return prompt | model | StrOutputParser()

    def ask_ai_image_prompt(self):
        prompt = self.prompt_builder.build_ai_image_prompt()
        self.__ask(prompt)

    def ask_description_prompt(self):
        prompt = self.prompt_builder.build_description_prompt()
        self.__ask(prompt)

    def __ask(self, prompt):
        logging.info(prompt)
        return self.chain.invoke({"input": prompt})
