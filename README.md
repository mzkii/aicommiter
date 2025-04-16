# aicommiter

🚀 A CLI tool that uses OpenAI to generate Git commit messages and pull requests automatically.

## 📦 1-line Installation

```bash
curl -sL https://your-host/aicommiter_cli.zip -o aicommiter.zip && unzip aicommiter.zip && cd aicommiter && pip install -r requirements.txt && pip install -e .
```

> Replace `your-host` with your actual file hosting URL if you're distributing the zip.

---

## 🛠 How to Use

### 1. Initialize a new branch (AI-suggested)

```bash
aicommiter init
```

### 2. Commit changes (AI-suggested commit messages in English)

```bash
aicommiter commit
```

### 3. Create a PR with AI-filled Japanese template (via GitHub CLI)

```bash
aicommiter pr
```

### 4. Preview PR content only (Japanese output)

```bash
aicommiter preview
```

---

## 🔐 OpenAI API Key

On first use, you'll be prompted to enter your `OPENAI_API_KEY`.  
It will be saved securely at `~/.aicommiter/openai_api_key` and reused automatically.

---

## ✅ Features

- [x] Compatible with OpenAI Python SDK >= 1.0.0
- [x] Git diff → AI-suggested branch names
- [x] AI-suggested commit messages (English)
- [x] AI-filled PR templates (Japanese)
- [x] Preview PR template before submitting
