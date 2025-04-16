import subprocess
import os
import questionary
from pathlib import Path
from openai import OpenAI

def get_saved_api_key():
    key_file = Path.home() / ".aicommiter" / "openai_api_key"
    if key_file.exists():
        return key_file.read_text().strip()
    else:
        return questionary.password("🔑 Enter your OpenAI API key:").ask()

def commit_changes():
    subprocess.run(["git", "add", "."], check=True)
    diff = subprocess.check_output(["git", "diff", "--cached"]).decode("utf-8")

    print("🤖 Asking OpenAI for commit message suggestions...")
    client = OpenAI(api_key=get_saved_api_key())

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a professional software engineer. Based on the following git diff, suggest 3 concise and clear English commit messages (1 line each). Only return the list of messages."
            },
            {"role": "user", "content": diff}
        ],
        temperature=0.5
    )

    candidates = response.choices[0].message.content.strip().split("\n")
    messages = [c.strip("- ").strip() for c in candidates if c.strip()]

    selected = questionary.select("💡 Choose a commit message:", choices=messages).ask()
    subprocess.run(["git", "commit", "-m", selected], check=True)
    print(f"✅ Commit complete: {selected}")
