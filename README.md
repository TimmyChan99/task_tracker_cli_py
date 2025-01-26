# Task Tracker CLI

Task Tracker is a command-line interface (CLI) application designed to help you manage and organize your tasks efficiently. It allows you to add, update, remove, and track the status of your tasks, all stored in a JSON file for persistence.

---

## Features

- **Add Tasks:** Add new tasks with a description.
- **Update Tasks:** Modify the description of an existing task.
- **Remove Tasks:** Delete a task by its ID.
- **Mark Tasks:** Change the status of a task to `in-progress` or `done`.
- **List Tasks:** Display all tasks or filter them by their status (`todo`, `in-progress`, or `done`).

---

## How It Works

The application uses:

- **Python's `argparse` module** for handling command-line arguments.
- **JSON file storage** to save and retrieve tasks.
- **Python dictionaries** for task management.

---

## Installation

1. Ensure you have Python 3.x installed on your machine.
2. Clone this repository or download the source code.
3. Navigate to the directory containing the `main.py` file.
4. Run the application from your terminal or command prompt.

---

## Usage

Run the application with the following command:

```bash
python3 task-cli main.py <action> [options]
```

### Available Actions

#### 1. Add a New Task
```bash
python3 task-cli main.py add "Task description"
```
- Example:
  ```bash
  python3 task-cli main.py add "Buy groceries"
  ```

#### 2. Update a Task
```bash
python3 task-cli main.py update <task_id> "Updated description"
```
- Example:
  ```bash
  python3 task-cli main.py update 1 "Buy groceries and cook dinner"
  ```

#### 3. Remove a Task
```bash
python3 task-cli main.py remove <task_id>
```
- Example:
  ```bash
  python3 task-cli main.py remove 1
  ```

#### 4. Mark a Task as Done
```bash
python3 task-cli main.py mark-done <task_id>
```
- Example:
  ```bash
  python3 task-cli main.py mark-done 2
  ```

#### 5. Mark a Task as In-Progress
```bash
python3 task-cli main.py mark-in-progress <task_id>
```
- Example:
  ```bash
  python3 task-cli main.py mark-in-progress 3
  ```

#### 6. List Tasks
```bash
python3 task-cli main.py list [status]
```
- **Status Options:**
  - `todo`: List tasks that are not started.
  - `in-progress`: List tasks currently in progress.
  - `done`: List completed tasks.

- Examples:
  ```bash
  python3 task-cli main.py list
  python3 task-cli main.py list done
  ```

---

## Task Storage

Tasks are stored in a JSON file named `tasks_list.json` in the current directory. If the file does not exist, it will be created automatically.

Each task is stored with the following structure:
```json
{
    "id": 1,
    "description": "Task description",
    "status": "todo",
    "createdAt": "dd/mm/yyyy",
    "updatedAt": "dd/mm/yyyy"
}
```
---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Contributing

Contributions are welcome! Feel free to fork this repository, create a feature branch, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

---

## Source

Challenge from [roadmap](https://roadmap.sh/projects/task-tracker)

---

## Contact

For questions, feedback, or suggestions, feel free to reach out via [LinkedIn](https://linkedin.com/in//fatima-ezzahra-elemenoun/) or open an issue on the GitHub repository.

