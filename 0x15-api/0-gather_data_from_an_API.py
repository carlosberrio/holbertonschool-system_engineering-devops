#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress.
Module that uses the 'https://jsonplaceholder.typicode.com/' REST API and
given employee ID, returns information about his/her ToDo list progress.
"""

import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    todos = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()
    done_tasks = [task for task in todos if task.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(done_tasks), len(todos)))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
