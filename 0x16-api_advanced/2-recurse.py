#!/usr/bin/python3

"""featch all title of all hot articles for a given subreddit
"""

import sys
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'user-agent': 'alxafrica'}
    params = {'after': after}

    res = requests.get(url=url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    data = res.json()
    listings = data.get('data').get('children')
    after = data.get('data').get('after')

    for article in listings:
        hot_list.append(article.get('data').get('title'))
    if after is not None:
        recurse(subreddit, hot_list=hot_list, after=after)

    return hot_list
