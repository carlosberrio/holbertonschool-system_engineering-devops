#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user = requests.get(url).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    tasks = requests.get(url).json()
    with open("{}.csv".format(user_id), "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user_id, user.get("username"),
                             task.get("completed"), task.get("title")])
