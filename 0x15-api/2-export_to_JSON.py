#!/usr/bin/python3
"""Exports to-do list information to JSON format."""
import requests
import json
import sys


def export_to_json(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_data = requests.get(user_url).json()
        username = user_data.get('username')
        todo_data = requests.get(todo_url).json()
        tasks = [{
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        } for task in todo_data]

        data = {str(employee_id): tasks}

        filename = f"{employee_id}.json"
        with open(filename, mode='w') as file:
            json.dump(data, file)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_json(employee_id)
