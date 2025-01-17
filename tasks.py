import json
import os
from typing import List

DATA_FILE = "tasks.json"


def load_tasks() -> List[dict]:
    """
    Loads tasks from the tasks.json file if it exists; otherwise returns an empty list.
    """
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            return []


def save_tasks(tasks: List[dict]) -> None:
    """
    Saves tasks to the tasks.json file.
    """
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)


def add_task(description: str) -> None:
    """
    Adds a new task to the list, defaulting to 'incomplete' status.
    """
    tasks = load_tasks()
    tasks.append({
        "description": description,
        "done": False
    })
    save_tasks(tasks)


def list_tasks() -> List[dict]:
    """
    Returns the list of all tasks from the file.
    """
    return load_tasks()


def complete_task(task_index: int) -> bool:
    """
    Marks a task as done given its 1-based index in the tasks list. 
    Returns True if successful, False otherwise.
    """
    tasks = load_tasks()
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["done"] = True
        save_tasks(tasks)
        return True
    return False


def remove_task(task_index: int) -> bool:
    """
    Removes a task from the tasks list by its 1-based index. 
    Returns True if successful, False otherwise.
    """
    tasks = load_tasks()
    if 1 <= task_index <= len(tasks):
        tasks.pop(task_index - 1)
        save_tasks(tasks)
        return True
    return False
