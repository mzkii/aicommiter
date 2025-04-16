import subprocess
import os
import questionary
from openai import OpenAI
from pathlib import Path
import re

def get_or_set_api_key():
    config_path = Path.home() / ".aicommiter"
    config_path.mkdir(exist_ok=True)
    key_file = config_path / "openai_api_key"

    if key_file.exists():
        return key_file.read_text().strip()
    else:
        api_key = questionary.password("🔑 OpenAI APIキーを入力してください:").ask()
        key_file.write_text(api_key)
        print(f"🔐 APIキーを {key_file} に保存しました。")
        return api_key

def extract_branch_slugs(text):
    # 箇条書きや番号付きリスト形式などを抽出（スラッグのみに絞る）
    lines = text.strip().split("\n")
    slugs = []
    for line in lines:
        match = re.match(r"^(?:[-*]|\d+\.)\s*(.+)$", line)
        if match:
            slug = match.group(1).strip()
            # 英数字とハイフンのみのスラッグ形式に限定
            if re.match(r"^[a-z0-9][a-z0-9\-]{2,}$", slug.replace(" ", "-").lower()):
                slugs.append(slug.replace(" ", "-").lower())
    return slugs

def init_branch():
    branch_types = ["feature", "fix", "chore", "refactor"]
    prefix = questionary.select("🔧 ブランチタイプを選択してください:", choices=branch_types).ask()

    print("📝 差分からブランチ名候補を生成中...")
    diff = subprocess.check_output(["git", "diff", "--cached"]).decode("utf-8")

    api_key = get_or_set_api_key()
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "あなたはGitのプロフェッショナルです。以下のgit diffの内容から、スラッグ形式（例: add-login-button）のブランチ名を3つ、番号付きまたは箇条書き形式で出力してください。説明文や見出しは不要です。"
            },
            {"role": "user", "content": diff}
        ],
        temperature=0.5
    )

    candidates = extract_branch_slugs(response.choices[0].message.content)
    if not candidates:
        print("⚠️ 有効なブランチ名候補が取得できませんでした。")
        return

    selected_slug = questionary.select("💡 ブランチ名候補:", choices=candidates).ask()
    branch_name = f"{prefix}/{selected_slug}"
    subprocess.run(["git", "checkout", "-b", branch_name])
    print(f"✅ 新しいブランチ '{branch_name}' に切り替えました")
