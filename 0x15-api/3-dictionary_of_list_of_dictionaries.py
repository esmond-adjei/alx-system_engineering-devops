#!/usr/bin/python3
"""Exports to-do list for all users to JSON format."""
import json
import requests


if __name__ == '__main__':
    url_users = "https://jsonplaceholder.typicode.com/users"
    url_todos = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(url_users).json()
    todos = requests.get(url_todos).json()

    tasks_by_user = {str(user['id']):
                     [{"username": user['username'],
                       "task": todo['title'],
                       "completed": todo['completed']}
                      for todo in todos
                      if todo['userId'] == user['id']]
                     for user in users}

    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        json.dump(tasks_by_user, file)
