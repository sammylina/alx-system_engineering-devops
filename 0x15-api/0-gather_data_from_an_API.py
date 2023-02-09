#!/usr/bin/python3
"""Fetch user's tasks from fake API
"""

if __name__ == '__main__':

    import requests as req
    import sys

    API_URL = 'https://jsonplaceholder.typicode.com/'

    user_res = req.get(API_URL+'users/{}'.format(sys.argv[1]))
    todo_req = req.get(API_URL+'users/{}/todos'.format(sys.argv[1]))

    name = user_res.json().get('name')
    todos = todo_req.json()

    completed_todos = [todo for todo in todos if todo.get('completed') is True]

    print('Employee {} is done with tasks({}/{}):'.format(name,
                                                          len(completed_todos),
                                                          len(todos)))
    for todo in completed_todos:
        print('\t {}'.format(todo.get('title')))
