#!/usr/bin/python3
# print number of subscribers from a given subreddit

import requests as req


def number_of_subscribers(subreddit):
    # print the number of subscriber

    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'alx'}

    res = req.get(url, headers=headers)
    if res.status_code == 200:
        return (res.json().get('data').get('subscribers'))

    return 0


if __name__ == '__main__':

    import sys

    subscribers = number_of_subscribers(sys.argv[1])
    print(subscribers)
