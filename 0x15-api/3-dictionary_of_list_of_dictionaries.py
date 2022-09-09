#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com to return information about all
employee's todo list progress
"""

import json
import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(url).json()
    url = 'https://jsonplaceholder.typicode.com/todos'
    todos = requests.get(url).json()
    user_dict = {}
    for user in users:
        user_dict[user.get('id')] = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                user_dict[user.get('id')].append({
                    'username': user.get('username'),
                    'task': task.get('title'),
                    'completed': task.get('completed')})
    with open('todo_all_employees.json', 'w') as f:
        json.dump(user_dict, f)
