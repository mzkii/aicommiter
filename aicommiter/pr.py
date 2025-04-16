import subprocess

def create_pr():
    commit_msg = subprocess.check_output(["git", "log", "-1", "--pretty=%B"]).decode("utf-8").strip()

    template = f"""## :star2: やったこと (必須。1行で簡潔に)
{commit_msg}

## :mag_right: 詳細 (必須)


## :bug: 確認したこと (必須)
- [ ] xxx

## :memo: 関連リンク


## :art: UI 差分
|BEFORE|AFTER|
|:--:|:--:|
|<img width="300" src=""/>|<img width="300" src=""/>|
"""

    with open(".tmp_pr_template.md", "w") as f:
        f.write(template)

    subprocess.run(["gh", "pr", "create", "--fill", "--body-file", ".tmp_pr_template.md"])
