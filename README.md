# 🧠 AutoFlow – AI-Powered Task Automation with GPT-4

**AutoFlow** is an AI agent-based system that turns natural language descriptions into Python automation scripts using GPT-4.

## 🚀 Features
- 🔹 **Basic Mode** – Generate a single Python script for any task
- 🔸 **Agent Mode** – Break complex tasks into subtasks and generate modular scripts
- 📦 CLI interface with `argparse`
- 🤖 Powered by OpenAI API (GPT-4)

## 🎯 Examples

**Basic Mode:**
```bash
python main.py --task "Download PDF files from a website" --mode basic
```

**Agent Mode:**
```bash
python main.py --task "Read CSV → calculate average → email result" --mode agents
```

## 🛠 Setup

### 1. Install requirements
```bash
pip install -r requirements.txt
```

### 2. Add your OpenAI API Key to `.env`
```
OPENAI_API_KEY=your_api_key_here
```

## 📁 Output

- In `basic` mode → outputs `generated_script.py`
- In `agents` mode → saves each subtask in `agents/agent_#.py`

## 💡 Use Case Examples
| Input Prompt | What Happens |
|--------------|---------------|
| "Monitor a folder for new files" | GPT writes Python script to watch file system |
| "Summarize a long PDF" | GPT generates a text summarizer using PyMuPDF |
| "Read data → filter → email" | Subtasked into 3 separate Python scripts |

## 📄 License
MIT

## 🤝 Contributing
Want to help? Fork the repo and open a PR!

## ✨ Created by MJ using GPT-4 and ❤️ for AI automation.
