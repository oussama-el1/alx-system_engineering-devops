#!/usr/bin/python3
"""import requests"""
import requests


def top_page_post(subreddit, after=None):
    """top 10 post in a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    if after:
        url += f'&after={after}'

    headers = {
        'User-Agent': 'alxapp/1.0 (by /u/oussamaelhadraoui777)'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return None, None
    else:
        data = response.json().get("data")
        return data.get('children'), data.get('after')


def recurse(subreddit, hot_list=[], after=None):
    """all post for subreddit"""
    posts, after = top_page_post(subreddit, after)
    if posts is not None:
        for post in posts:
            hot_list.append(post['data']['title'])
        if after:
            recurse(subreddit, hot_list, after)
    if len(hot_list) == 0:
        return None
    else:
        return hot_list
