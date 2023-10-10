#!/usr/bin/python3
"""
recursively get the hot list
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """recursively get hot list"""

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    params = {'limit': 100, 'after': after} if after else {'limit': 100}
    headers = {'User-Agent': 'MyRedditBot'}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get('data')
        children = data.get('children')

        if children:
            hot_list.extend([child.get('data').get('title')
                            for child in children])
            after = data.get('after')

            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return hot_list
    else:
        return None
