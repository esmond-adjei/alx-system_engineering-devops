#!/usr/bin/python3
"""
function that queries the Reddit API and prints
the titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Get top ten hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-agent": "Custom"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        [print(child.get("data").get("title"))
            for child in response.json().get("data").get("children")]
    else:
        print(None)
