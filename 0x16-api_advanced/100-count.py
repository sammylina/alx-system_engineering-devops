#!/usr/bin/python3
""" Parse all hot articles title of subreddit and count
the number of given keywords
"""

import requests as req


def count_words(subreddit, word_list, count_list={}, after=None):
    """count function
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'alx'}
    params = {'after': after}

    res = req.get(url, headers=headers, params=params, allow_redirects=False)

    if res.status_code == 200:
        data = res.json().get('data')
        after = data.get('after')
        for reddit in data.get('children'):
            title = reddit.get('data').get('title')
            count_list = count(word_list, title, count_list)
        if after:
            return count_words(subreddit,
                               word_list,
                               count_list=count_list,
                               after=after)
        else:
            print_count_list(count_list)
            return
    else:
        print("")
        return


def print_count_list(count_list):
    """print count
    """
    if len(count_list) != 0:
        sorted_list = sorted(count_list.items(),
                             key=lambda item: (item[1], item[0]),
                             reverse=True)
        new_list = {}
        for item in sorted_list:
            if item[1]:
                print('{}: {}'.format(item[0], item[1]))
    else:
        print('')


def count(word_list, title, count_list):
    """count
    """
    title = title.lower().split()
    for word in word_list:
        if word.lower() in title:
            count = len([t for t in title if word.lower() == t])
            if count_list.get(word.lower()):
                count_list[word.lower()] += count
            else:
                count_list[word.lower()] = count
    return count_list
