#!/usr/bin/python3
"""import requests"""
import requests


def number_of_subscribers(subreddit):
    "number_of_subscribers of a subreddit"
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'alxapp/1.0 (by /u/oussamaelhadraoui777)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    else:
        data = response.json()
        subscribers = data.get('data')['subscribers']
        return subscribers
