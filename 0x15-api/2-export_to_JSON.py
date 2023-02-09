#!/usr/bin/python3
"""Fetch user's todo information from REST API
and export it to json file
"""

if __name__ == '__main__':

    import json
    import requests as req
    import sys

    API_URL = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]

    user_res = req.get(API_URL+'users/{}'.format(user_id))
    todo_req = req.get(API_URL+'users/{}/todos'.format(user_id))

    username = user_res.json().get('username')
    todos = todo_req.json()

    new_todos = [{'task': todo.get('title'),
                  'completed': todo.get('completed'),
                  "username": username} for todo in todos]

    file_name = '{}.json'.format(user_id)
    with open(file_name, 'w') as jsonfile:
        json.dump({user_id: new_todos}, jsonfile)
