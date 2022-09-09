#!/usr/bin/python3
"""
Python script that, using a REST API,
returns information about his/her todo list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":

    todos_url = "https://jsonplaceholder.typicode.com/todos/"
    users_url = "https://jsonplaceholder.typicode.com/users/"
    id = argv[1]

    name = requests.get(users_url + id).json()
    task = requests.get(todos_url, params={"userId": id}).json()
    total_task = requests.get(
        todos_url,
        params={
            "userId": id,
            "completed": "true"
        }
    ).json()

    print("Employee {} is done with tasks({}/{}):".format(
        name.get("name"),
        len(total_task),
        len(task)
    ))

    for task in total_task:
        print("\t {}".format(task.get("title")))
