import argparse
from datetime import datetime
import json
from random import choice

Actions = ['add', 'update', 'remove', 'mark-done', 'mark-in-progress', 'list']
TASK_STATUS = ['todo', 'in-progress', 'done']
added_tasks = 0

# File handling
def get_tasks_list():
    try:
        # Create a JSON file and return empty list
        open('tasks_list.json', 'x')
        return []
    except:
        # Read existing JSON file and get content
        tasks_file = open('tasks_list.json', 'r')
        read_content = tasks_file.read()
        if read_content:
            return  json.loads(read_content)
        else:
            return []

def update_tasks_list_json(updated_list):
    if not len(updated_list):
        print('Your tasks list is empty.')
        return

    try:
        with open('tasks_list.json', 'w') as json_file:
            json.dump(updated_list, json_file, indent=4)
    except:
        print('Your tasks list is empty.')

# Top level command
parser = argparse.ArgumentParser()
parser.add_argument('task-cli')
subparsers = parser.add_subparsers(dest='actions', title='subcommand action on tasks')

# Add task Sub Command
parser_add = subparsers.add_parser('add', help='Add new task')
parser_add.add_argument('description', type=str, help='Task description')

# Update task Sub Command
parser_update = subparsers.add_parser('update', help='Update task')
parser_update.add_argument('id', type=int, help='Task to update id')
parser_update.add_argument('description', type=str, help='Updated task description')

# Remove task Sub Command
parser_remove = subparsers.add_parser('remove', help='Remove task')
parser_remove.add_argument('id', type=int, help='Task to remove id')

# Mark as done task Sub Command
parser_mark_done = subparsers.add_parser('mark-done', help='Mark task as done')
parser_mark_done.add_argument('id', type=int, help='Task to mark as done id')

# Mark in progress task Sub Command
parser_mark_in_progress = subparsers.add_parser('mark-in-progress', help='Mark task in progress')
parser_mark_in_progress.add_argument('id', type=int, help='Task to mark as in progress id')

# List tasks Sub Command
parser_list_tasks = subparsers.add_parser('list', help='List tasks')
list_tasks_subparsers = parser_list_tasks.add_subparsers(dest='status')
parser_list_done_tasks = list_tasks_subparsers.add_parser('done', help='List done tasks')
parser_list_todo_tasks = list_tasks_subparsers.add_parser('todo', help='List todo tasks')
parser_list_in_progress_tasks = list_tasks_subparsers.add_parser('in-progress', help='List in progress tasks')

command = parser.parse_args()

action_type = command.actions

def generate_id():
    tasks_list = get_tasks_list()
    return len(tasks_list) + 1

# Actions
def add_task(description):
    task = {
        'id': generate_id(),
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().strftime('%d/%m/%Y'),
        'updatedAt': None
    }
    tasks_list = get_tasks_list()
    tasks_list.append(task)
    update_tasks_list_json(tasks_list)

def update_task(task_id, description):
    tasks_list = get_tasks_list()
    for task in tasks_list:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().strftime('%d/%m/%Y')
            break
    update_tasks_list_json(tasks_list)

def remove_task(task_id):
    tasks_list = get_tasks_list()
    for task in tasks_list:
        if task['id'] == task_id:
            tasks_list.remove(task)
            break
    update_tasks_list_json(tasks_list)

def update_task_status(task_id, status):
    tasks_list = get_tasks_list()
    for task in tasks_list:
        if task['id'] == task_id:
            task['status'] = status
            break
    update_tasks_list_json(tasks_list)

def filter_by_status(task, status):
    return task['status'] == status

def list_tasks(status):
    tasks_list = get_tasks_list()
    if status:
       return [task for task in tasks_list if task['status'] == status]
    return tasks_list

# Check actions
if action_type in Actions:
    if action_type == 'add':
        add_task(command.description)
    elif action_type == 'update':
        update_task(command.id, command.description)
    elif action_type == 'remove':
        remove_task(command.id)
    elif action_type == 'mark-done':
        update_task_status(command.id, 'done')
    elif action_type == 'mark-in-progress':
        update_task_status(command.id, 'in-progress')
    elif action_type == 'list':
        print(json.dumps(list_tasks(command.status), indent=2))

else:
    print('Enter a valid action: add, update or remove')
