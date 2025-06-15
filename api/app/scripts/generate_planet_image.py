import openai
from openai import OpenAI
import json
import requests
from PIL import Image
from io import BytesIO
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import HumanMessagePromptTemplate
import os
from langchain_core.messages import HumanMessage
import base64
import httpx
from dotenv import load_dotenv
load_dotenv()


#フロント側からの入力値をここで受け取る




#画像作成プロンプトを作成するためのシステムプロンプト
system_prompt = '''\
あなたはAIに関する経験が豊富な、優秀なプロンプトエンジニアです。 \
以下の「プロンプト作成のルール」に従って、\
DALL-E3に効果的な指示を与えるためのプロンプトを考えてください。

***プロンプト作成のルール***
具体的で明確な表現をすること
ユーザーの入力に基づいて、繊細で想像力豊かな画像を作成すること
ビジュアルが鮮明になるよう色・形・動き・状況などを具体的に記述すること
指示された内容自体は含まないこと
\
'''

#画像作成プロンプトを作成する関数
def make_prompt(text):
  prompt = ChatPromptTemplate.from_messages(
      [
          ("system", system_prompt),
          ("human", "{input}"),
      ]
      )
  model = ChatOpenAI(model="gpt-4o", temperature=0.5, openai_api_key=os.getenv(OPENAI_API_KEY))

  chain = prompt | model | StrOutputParser()
  prompt_img_gen = chain.invoke({"input": text})
  return prompt_img_gen

prompt_text = make_prompt(answers)

#画像作成プロンプトに基づいて画像作成
def generate_image(prompt_text): 
  res = client.images.generate(
    model="dall-e-3",
    prompt=prompt_text,
    size="1024x1024",
    quality="standard",
    response_format="url",
    style="natural"
    )
  return res.data[0].url

image_url = generate_image(prompt_text)
img_response = requests.get(image_url)
#画像として読み込み
img = Image.open(BytesIO(img_response.content))