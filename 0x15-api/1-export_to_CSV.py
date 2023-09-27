#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 1:
        print(f"Usage: {sys.argv[0]} <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    URL = "https://jsonplaceholder.typicode.com/"
    user = requests.get(URL + f"users/{user_id}").json()
    username = user.get("username")
    todos = requests.get(URL + "todos", params={"userId": user_id}).json()

    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username, task.get("completed"),
                            task.get("title")])
