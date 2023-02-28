#!/usr/bin/python3
"""print all hot articles title of a given subreddit
"""


import requests as req


def recurse(subreddit, hot_list=[], after=None):
    """print all hot articles title of a given subreddit
    """

    url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'alx'}
    params = {'limit': '100', 'after': after}

    res = req.get(url, headers=headers, params=params)
    print(res.url)
    if res.status_code == 200:

        data = res.json().get('data')
        after = data.get('after')
        for reddit in data.get('children'):
            hot_list.append(reddit.get('data').get('title'))
        if after:
            return recurse(subreddit, hot_list=hot_list, after=after)
    else:
        return None

    return hot_list
