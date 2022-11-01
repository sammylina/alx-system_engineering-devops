#!/usr/bin/python3

"""fetch number of subscribers of a specific subreddit
"""

import requests


def number_of_subscribers(subreddit):
    API_URL = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    headers = {'user-agent': 'reddit'}

    res = requests.get(url=API_URL, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return 0
    data = res.json()
    return data.get('data').get('subscribers')
