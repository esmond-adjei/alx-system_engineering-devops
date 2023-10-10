#!/usr/bin/python3
"""
function that queries the Reddit API
and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Get totla number of subscribers for a give subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "custom"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
