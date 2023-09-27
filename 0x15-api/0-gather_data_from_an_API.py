#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


def get_user_info(user_id):
    """gets user info and user's todo tasks"""
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + f"users/{user_id}").json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    return user, todos


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <user_id>")
        sys.exit(1)

    user, todos = get_user_info(sys.argv[1])
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
