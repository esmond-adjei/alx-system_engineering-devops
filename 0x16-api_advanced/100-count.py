#!/usr/bin/python3
"""count all keywords in articles"""

import requests


def count_words(subreddit, word_list, word_counts=None, after=None):
    """count all keywords in articles"""

    if word_counts is None:
        word_counts = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    headers = {'User-Agent': 'MyRedditBot'}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get('data')
        children = data.get('children')
        after = data.get('after') if children else None
        titles = [child.get('data').get('title').lower()
                  for child in children] if children else []

        for title in titles:
            for word in word_list:
                word = word.lower()
                if title.count(word) > 0:
                    word_counts[word] = word_counts.get(word, 0)\
                        + title.count(word)

        if after:
            return count_words(subreddit, word_list, word_counts, after)

    if word_counts:
        sorted_word_counts = sorted(word_counts.items(),
                                    key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_counts:
            print(f"{word}: {count}")
