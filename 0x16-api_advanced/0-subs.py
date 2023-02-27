#!/usr/bin/python3
"""print number of subscribers from a given subreddit
"""

import requests as req
import sys


def number_of_subscribers(subreddit):
    """print the number of subscriber
    """

    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'alx'}

    res = req.get(url, headers=headers)
    if res.status_code == 200:
        return (res.json().get('data').get('subscribers'))

    return 0


if __name__ == '__main__':

    subreddit = sys.argv[1] if (len(sys.argv) > 1) else ""
    subscribers = number_of_subscribers(subreddit)
    print(subscribers)
