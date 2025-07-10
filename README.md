# 🤖 AutoFlow – AI-Powered Python Workflow Generator

**AutoFlow** is an AI coding assistant that transforms plain language task descriptions into real, working Python scripts using GPT-4.  
It supports both **single script generation** and **agent-based breakdown**, enabling you to automate complex workflows effortlessly.

---

## 🔍 Why AutoFlow?

This tool was built as a portfolio project for the **"Vibe Coder – AI Engineer"** role at [HUMAIN](https://humain.ai), where AI agents are the future of software development. AutoFlow showcases how LLMs like GPT-4 can:
- Understand human intent
- Break it down into actionable steps
- Generate working, production-ready code

---

## 🚀 Features

| Mode         | Description                                                  |
|--------------|--------------------------------------------------------------|
| `basic`      | Generates one Python script directly from your task          |
| `agents`     | Breaks the task into subtasks and generates scripts per step |

- 🧠 Uses GPT-4 via OpenAI API
- 🛠 Clean CLI interface (argparse)
- 📁 Saves scripts automatically
- 🔄 Modular agents for flexible workflows

---

## 💡 Examples

### 🧾 Basic Mode

```bash
python main.py --task "Read a CSV file and calculate average salary" --mode basic
```

🛠 Output:
- One script: `generated_script.py`

---

### 🔁 Agent Mode

```bash
python main.py --task "Read a CSV → filter high salaries → send summary email" --mode agents
```

🛠 Output:
- `agents/agent_1.py` → CSV reader
- `agents/agent_2.py` → Filter logic
- `agents/agent_3.py` → Email sender

---

## 🛠 Setup Instructions

1. **Install dependencies**

```bash
pip install -r requirements.txt
```

2. **Add your OpenAI key in `.env`**

```env
OPENAI_API_KEY=your_openai_key_here
```

3. **Run the CLI**

```bash
python main.py --task "Describe your task" --mode [basic|agents]
```

---

## 🔐 .env Example

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 📂 Project Structure

```
autoflow-ai-agent/
├── agents/              # Holds modular agent scripts
├── main.py              # CLI entry point
├── prompts.py           # Prompt templates
├── utils.py             # OpenAI interaction
├── requirements.txt
└── .env                 # Your OpenAI key
```

---

## 🧠 Technologies

- GPT-4 via OpenAI API
- Python 3.10+
- LangChain-like task structuring (custom)
- CLI via argparse
- dotenv for secure key management

---

## 📄 License

MIT

---

## 🙋 About the Author

**AbdulrahmanAlbaz** – M.Eng. in Applied AI for Digital Production Management  
💼 Applying for the "Vibe Coder" role @ HUMAIN  
📫 Contact: [Your Email or GitHub Profile]

---

## ✨ Want to See It in Action?

Check out the example prompts or run your own.  
This project was built to demonstrate how **AI agents + prompt engineering** can change the way we build software.

---

> 🔗 Let's build the future of agent-driven development together.
