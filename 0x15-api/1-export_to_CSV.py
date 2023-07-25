#!/usr/bin/python3
"""Exports to-do list information to CSV format."""
import csv
import requests
import sys


def export_to_csv(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_data = requests.get(user_url).json()
        name = user_data.get('username')

        todo_data = requests.get(todo_url).json()
        filename = f"{employee_id}.csv"

        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            [writer.writerow(
                [employee_id, name, task.get("completed"), task.get("title")])
             for task in todo_data]
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)
