#!/usr/bin/python3
"""print top 10 reddits of a given subreddit
"""

import requests as req
import sys


def top_ten(subreddit):
    """print top 10 reddits
    """

    url = 'https://reddit.com/r/{}/top.json'.format(subreddit)
    headers = {'User-Agent': 'alx'}
    q_str = {'limit': '10'}

    res = req.get(url, headers=headers, params=q_str)
    if res.status_code == 200:
        for reddit in res.json().get('data').get('children'):
            print(reddit.get('data').get('title'))
        return 0

    print(None)


if __name__ == '__main__':

    subreddit = sys.argv[1] if (len(sys.argv) > 1) else ""
    top_ten(subreddit)
