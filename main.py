import argparse
import datetime

tasks_list = []
Actions = ['add', 'update', 'remove']
TASK_STATUS = ['todo', 'in-progress', 'done']
added_tasks = 0

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
parser_update = subparsers.add_parser('remove', help='Remove task')
parser_update.add_argument('id', type=int, help='Task to remove id')

command = parser.parse_args()
print(command)

action_type = command.actions

# Actions
def add_task(description):
    task = {
        'id': added_tasks + 1,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.datetime.now(),
        'updatedAt': None
    }
    tasks_list.append(task)

def update_task(task_id, description):
    for task in tasks_list:
        if task['id'] == task_id:
            task['description'] = description
            break

def remove_task(task_id):
    for task in tasks_list:
        if task['id'] == task_id:
            tasks_list.remove(task)
            break

# Check actions
if action_type in Actions:
    if action_type == 'add':
        add_task(command.description)
    elif action_type == 'update':
        update_task(command.id, command.description)
    else:
        remove_task(command.id)
else:
    print('Enter a valid action: add, update or remove')
print(tasks_list)
