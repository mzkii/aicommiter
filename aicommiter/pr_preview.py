import subprocess
from pathlib import Path
from openai import OpenAI
import os

def get_saved_api_key():
    key_file = Path.home() / ".aicommiter" / "openai_api_key"
    if key_file.exists():
        return key_file.read_text().strip()
    else:
        return os.getenv("OPENAI_API_KEY", "")

def preview_pr():
    diff = subprocess.check_output(["git", "diff", "--cached"]).decode("utf-8")
    client = OpenAI(api_key=get_saved_api_key())

    print("🤖 PRテンプレートをAIでプレビュー出力中...")

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "あなたはプロダクト開発のエンジニアです。以下のgit diffから、PRテンプレートの各項目（やったこと、詳細、確認したこと）を日本語で埋めてください。テンプレート形式で出力してください。"},
            {"role": "user", "content": diff}
        ],
        temperature=0.5
    )

    print(response.choices[0].message.content.strip())
