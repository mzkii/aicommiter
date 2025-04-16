# aicommiter

🚀 A CLI tool that uses OpenAI to generate Git commit messages and pull requests automatically.

## 📦 1-line Installation

```bash
curl -sL https://your-host/aicommiter_cli_commit_fixed_final.zip -o aicommiter.zip && unzip aicommiter.zip && cd aicommiter && pip install -r requirements.txt && pip install -e .
```

> Replace `your-host` with your actual file hosting URL if you're distributing the zip.

---

## 🛠 How to Use

### 1. Initialize a new branch (with AI-suggested names)

```bash
aicommiter init
```

### 2. Commit changes (AI-suggested commit messages)

```bash
aicommiter commit
```

### 3. Create a PR (using a generated template and GitHub CLI)

```bash
aicommiter pr
```

---

## 🔐 OpenAI API Key

When running for the first time, you'll be asked to enter your `OPENAI_API_KEY`.  
It will be saved securely at `~/.aicommiter/openai_api_key` and reused automatically.

---

## ✅ Features

- [x] Compatible with OpenAI Python SDK >= 1.0.0
- [x] Generates branch names based on git diff
- [x] AI-generated commit message selection
- [x] PR body templating with `gh pr create` support

---

This CLI makes your Git workflow faster, cleaner, and powered by AI ✨
