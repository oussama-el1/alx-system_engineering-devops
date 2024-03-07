import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """count_words"""
    if counts is None:
        counts = {}

    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json?limit=100"\
            .format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}"\
            .format(subreddit, after)

    headers = {
        'User-Agent': 'MyRedditApp/1.0 (by /u/MyRedditUsername)'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return

    data = response.json().get("data")
    posts = data.get('children')
    after = data.get('after')

    for post in posts:
        title = post.get('data').get('title').lower()
        for word in word_list:
            occurrences = title.count(word.lower())
            if occurrences > 0:
                counts[word.lower()] = counts.get(word.lower(), 0)
                +occurrences

    if after is not None:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
