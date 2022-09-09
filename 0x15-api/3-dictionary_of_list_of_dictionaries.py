#!/usr/bin/python3
"""
Python script that, using a REST API,
export data in the JSON format.
"""

import json
import requests


if __name__ == "__main__":

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users/"

    all_users = requests.get(users_url).json()

    with open('todo_all_employees.json', 'w') as outfile:
        json.dump({i.get("id"): [{
            "task": tt.get("title"),
            "completed": tt.get("completed"),
            "username": i.get("username")}
            for tt in requests.get(todos_url, params={
                "userId": i.get("id")}).json()]
            for i in all_users}, outfile)
