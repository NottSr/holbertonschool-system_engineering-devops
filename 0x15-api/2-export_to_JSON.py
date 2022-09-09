#!/usr/bin/python3
"""
Python script that, using a REST API,
export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    todos_url = "https://jsonplaceholder.typicode.com/todos/"
    users_url = "https://jsonplaceholder.typicode.com/users/"
    id = argv[1]

    name = requests.get(users_url + id).json()
    task = requests.get(todos_url, params={"userId": id}).json()
    total_task = requests.get(
        todos_url, params={"userId": id, "completed": "true"}).json()

    with open(id + '.json', 'w') as outfile:
        json.dump({id: [{"task": tt.get("title"), "completed": tt.get(
            "completed"), "username": name} for tt in task]}, outfile)
