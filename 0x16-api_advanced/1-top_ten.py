#!/usr/bin/python3

"""print the titles of top ten hot poste of a subreddit
"""
import requests


def top_ten(subreddit):

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'user-agent': 'alxafrica'}
    params = {'limit': 10}

    res = requests.get(url=url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        print(None)
    else:
        data = res.json()
        for key in data.get('data').get('children'):
            print(key.get('data')['title'])
