#!/bin/bash

set -euo pipefail

echo "🔍 差分を取得中..."
git add .
git diff --cached > diff.patch

echo "🤖 OpenAIでコミットメッセージを生成中..."
message=$(python3 scripts/generate_commit.py diff.patch)

echo "💡 コミットメッセージ候補:"
echo "$message" | nl

commit_msg=$(echo "$message" | head -n 1)

echo "📝 採用されたコミットメッセージ: $commit_msg"

read -p "🌿 ブランチ名を入力してください (例: feature/add-xxx): " branch
git checkout -b "$branch"

git commit -m "$commit_msg"

git push --set-upstream origin "$branch"

pr_template=".tmp_pr_template.md"
python3 scripts/generate_pr_template.py "$commit_msg" > "$pr_template"

echo "🚀 GitHub Pull Request を作成中..."
gh pr create --fill --body-file "$pr_template"
