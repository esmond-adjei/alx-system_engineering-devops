#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 1:
        print(f"Usage: {sys.argv[0]} <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    URL = "https://jsonplaceholder.typicode.com/"
    user = requests.get(URL + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(URL + "todos", params={"userId": user_id}).json()

    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump({user_id: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            } for task in todos]}, jsonfile)
