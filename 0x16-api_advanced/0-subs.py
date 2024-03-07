#!/usr/bin/python3
"""import requests"""
import requests


def number_of_subscribers(subreddit):
    "number_of_subscribers of a subreddit"
    if subreddit is None or type(subreddit) != str or subreddit == "":
        return 0
    else:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {
            'User-Agent': 'alxapp/1.0 (by /u/oussamaelhadraoui777)'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
