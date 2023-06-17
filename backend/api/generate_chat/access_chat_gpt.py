import os
import openai

# openai.organization = "org-jSDWwxj0g5oYWyeLkGvfFJms"
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"
model_name = "gpt-3.5-turbo-0301"
negative_characters = "、".join(["ツンデレお嬢様"])
question = f"""
キャラクターの性格を下記のフォーマットで考えてください．
なお，戦士や神官などのファンタジーな要素は含まないでください．
また，これらの性格({negative_characters})も含まないでください．
性別は明記しないでください。

【性格】
おっとりしたお嬢様，など

【一人称】
わたくし，など

【二人称】
あなた，など

【食べ物の好き嫌い】
いちごショートケーキなどの甘いものが好きで，コーヒーなどの苦いものが嫌い，など

【性格の詳細】
行動原理や特徴的な一面など

【口調】
「それは……どういう意味だ？」
「ふむ、それはおかしいな。」，など

【口癖】
「やれやれ、またか。」
「そうか、なるほど。」
「ああ、それが答えか。」，など
"""

response = openai.ChatCompletion.create(
    model=model_name,
    messages=[
        {"role": "user", "content": question},
    ],
)

character = response["choices"][0]["message"]["content"].encode("utf-8").decode("utf-8")

print()
