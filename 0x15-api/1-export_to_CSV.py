#!/usr/bin/python3
"""Fetch user's tasks from fake API
"""

if __name__ == '__main__':

    import csv
    import requests as req
    import sys

    API_URL = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]

    user_res = req.get(API_URL+'users/{}'.format(user_id))
    todo_req = req.get(API_URL+'users/{}/todos'.format(user_id))

    name = user_res.json().get('username')
    todos = todo_req.json()

    completed_todos = [todo for todo in todos if todo.get('completed') is True]

    todo_headers = ["userId", "username", "completed", "title"]
    with open('{}.csv'.format(user_id), 'w', encoding='UTF8') as csvfile:
        writer = csv.DictWriter(csvfile,
                                fieldnames=todo_headers,
                                extrasaction='ignore',
                                quoting=csv.QUOTE_ALL,
                                quotechar='"')
        for todo in todos:
            todo['username'] = name
            writer.writerow(todo)
