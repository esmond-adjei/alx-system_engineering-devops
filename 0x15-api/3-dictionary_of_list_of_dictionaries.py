#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    users = requests.get(URL + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            user.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            } for task in requests.get(URL + "todos",
                                       params={
                                           "userId": user.get("id")
                                            }).json()]
            for user in users}, jsonfile)
