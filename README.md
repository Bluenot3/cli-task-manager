# cli-task-manager# CLI Task Manager

A simple command-line task manager in Python. Quickly add, list, complete, and remove tasks, all stored locally in a JSON file.

## Setup

1. **Clone the repo**:
    ```bash
    git clone https://github.com/<your_username>/cli-task-manager.git
    cd cli-task-manager
    ```
2. **(Optional) Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. **Install any dependencies** (if you add them to `requirements.txt`):
    ```bash
    pip install -r requirements.txt
    ```
4. **Run**:
    ```bash
    python main.py [command] [arguments]
    ```

## Usage

```bash
python main.py add "Task description"
python main.py list
python main.py done <task_number>
python main.py remove <task_number>
