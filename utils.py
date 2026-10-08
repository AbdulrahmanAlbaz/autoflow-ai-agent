import ast
import os
import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def generate_script(prompt, model=None):
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("Set OPENAI_API_KEY in your environment or .env file.")
    client = OpenAI(timeout=60.0, max_retries=2)
    response = client.chat.completions.create(
        model=model or os.getenv("OPENAI_MODEL", "gpt-4"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3, max_tokens=2000,
    )
    if response.choices[0].finish_reason == "length":
        raise ValueError("Model output was truncated; simplify the task.")
    text = response.choices[0].message.content
    if not text or not text.strip():
        raise ValueError("The model returned an empty response.")
    return text.strip()

def validate_code(text):
    code = text.strip()
    if code.startswith("```"):
        lines = code.splitlines()
        if lines[-1].strip() != "```":
            raise ValueError("Unclosed Markdown code block.")
        code = "\n".join(lines[1:-1])
    if not code.strip():
        raise ValueError("No Python code returned.")
    ast.parse(code)
    return code + "\n"

def parse_subtasks(text):
    tasks = []
    for line in text.splitlines():
        match = re.match(r"^\s*(?:\d+[.)]|[-*•])\s+(.+)$", line)
        if match:
            tasks.append(match.group(1).strip())
    if not tasks:
        raise ValueError("No subtasks found in the model response.")
    return tasks
