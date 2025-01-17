import sys
from tasks import add_task, list_tasks, complete_task, remove_task


def print_usage():
    """
    Prints usage instructions for the CLI tool.
    """
    usage = """
Usage:
  python main.py add "Task description"   # Add a new task
  python main.py list                     # List all tasks
  python main.py done <task_number>       # Mark task_number as done
  python main.py remove <task_number>     # Remove a task

Examples:
  python main.py add "Buy groceries"
  python main.py list
  python main.py done 2
  python main.py remove 3
"""
    print(usage)


def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 3:
            print("Please provide a task description in quotes, e.g.:")
            print("  python main.py add \"Buy groceries\"")
            sys.exit(1)
        description = " ".join(sys.argv[2:]).strip("\"")
        add_task(description)
        print(f"Added task: {description}")

    elif command == "list":
        tasks = list_tasks()
        if not tasks:
            print("No tasks found. Add one using 'python main.py add \"Task description\"'")
        else:
            print("Your Tasks:")
            for idx, task in enumerate(tasks, start=1):
                status = "✅" if task["done"] else "❌"
                print(f"{idx}. [{status}] {task['description']}")

    elif command == "done":
        if len(sys.argv) < 3:
            print("Please provide the task number, e.g.:")
            print("  python main.py done 2")
            sys.exit(1)
        try:
            task_num = int(sys.argv[2])
            success = complete_task(task_num)
            if success:
                print(f"Task {task_num} marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please provide a valid task number.")

    elif command == "remove":
        if len(sys.argv) < 3:
            print("Please provide the task number, e.g.:")
            print("  python main.py remove 2")
            sys.exit(1)
        try:
            task_num = int(sys.argv[2])
            success = remove_task(task_num)
            if success:
                print(f"Task {task_num} removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please provide a valid task number.")

    else:
        print_usage()


if __name__ == "__main__":
    main()
