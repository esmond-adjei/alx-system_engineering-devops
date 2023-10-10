#!/usr/bin/python3
"""
 a recursive function that queries the Reddit API
 and returns a list containing the titles of all
 hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
     returns a list containing titles of all hot articles
     for a given subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom"}
    params = {"limit": 100}

    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json().get("data")
        after = data.get("after")

        if after:
            hot_list.extend([child.get("data").get("title")
                            for child in data.get("children")])

            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
