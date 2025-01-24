import argparse

tasks_list = []
actions = ['add', 'update', 'remove']

parser = argparse.ArgumentParser()
parser.add_argument('action', nargs=2, help='Actions')

command = parser.parse_args()
action_type = command.action[0]

if action_type in actions:
    if action_type == 'add':
        print('adding')
    elif action_type == 'update':
        print('updating')
    else:
        print('removing')
else:
    print('Enter a valid action: add, update or remove')
