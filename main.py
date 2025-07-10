import argparse
import os
from prompts import build_prompt, task_breakdown_prompt, subtask_script_prompt
from utils import generate_script

def generate_basic(task):
    prompt = build_prompt(task)
    code = generate_script(prompt)
    print("\n🧠 Generated Script:\n")
    print(code)

    save = input("\n💾 Save script as generated_script.py? (y/n): ").strip().lower()
    if save == 'y':
        with open("generated_script.py", "w") as f:
            f.write(code)
        print("✅ Script saved to generated_script.py")

def generate_agents(task):
    print("\n🔍 Breaking task into subtasks...")
    breakdown = generate_script(task_breakdown_prompt(task))
    subtasks = [line.split('. ', 1)[1] for line in breakdown.strip().splitlines() if '. ' in line]

    print("\n🛠 Generating agents...\n")
    os.makedirs("agents", exist_ok=True)

    for i, sub in enumerate(subtasks, 1):
        print(f"⚙️ Subtask {i}: {sub}")
        code = generate_script(subtask_script_prompt(sub))
        filename = f"agents/agent_{i}.py"
        with open(filename, "w") as f:
            f.write(code)
        print(f"✅ Saved: {filename}")

    print("\n🎉 All agent scripts saved in 'agents/' folder.")

def main():
    parser = argparse.ArgumentParser(description="AutoFlow: AI-Powered Python Code Generator")
    parser.add_argument('--task', type=str, required=True, help="Describe the task you want to automate")
    parser.add_argument('--mode', type=str, choices=['basic', 'agents'], default='basic',
                        help="Choose generation mode: basic (single script) or agents (modular tasks)")

    args = parser.parse_args()

    if args.mode == 'basic':
        generate_basic(args.task)
    elif args.mode == 'agents':
        generate_agents(args.task)

if __name__ == "__main__":
    main()
