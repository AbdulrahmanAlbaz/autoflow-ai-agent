def build_prompt(task_description):
    return f"""
You are a Python coding assistant.

Write a clear, well-commented Python script to accomplish the following task:

"{task_description}"

Return only the Python code without explanation.
"""

def task_breakdown_prompt(task):
    return f"""
Break the following task into smaller subtasks that can be handled by separate Python scripts.

Task: "{task}"

Return a list of subtasks in this format:

1. Subtask description
2. Subtask description
...
"""

def subtask_script_prompt(subtask):
    return f"""
You are an AI Python agent.

Write a well-commented Python script to handle this task:

"{subtask}"

Return only the code.
"""
