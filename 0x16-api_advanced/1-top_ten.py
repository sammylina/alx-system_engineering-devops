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

import sys

if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
