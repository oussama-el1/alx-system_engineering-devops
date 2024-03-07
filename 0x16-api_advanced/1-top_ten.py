#!/usr/bin/python3
"""import requests"""
import requests


def top_ten(subreddit):
    """top 10 post in a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        'User-Agent': 'alxapp/1.0 (by /u/oussamaelhadraoui777)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return 0
    else:
        data = response.json().get("data")
        posts = data.get('children')
        for post in posts:
            print(post['data']['title'])
