import openai
import sys
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

with open(sys.argv[1], "r") as f:
    diff = f.read()

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "あなたはプロのエンジニアです。以下のgit diffから、1行で端的に説明するコミットメッセージを3つ日本語で提案してください。"
        },
        {"role": "user", "content": diff}
    ],
    temperature=0.5
)

choices = response["choices"][0]["message"]["content"]
print(choices)
