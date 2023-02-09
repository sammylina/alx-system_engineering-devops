#!/usr/bin/python3
"""fetch all users and their tasks from REST API
and export to json file
"""

if __name__ == '__main__':

    import json
    import requests as req

    API_URL = 'https://jsonplaceholder.typicode.com/'

    res = req.get(API_URL+'users')
    users = res.json()

    response_dict = {}
    for user in users:
        user_id = user.get('id')
        res = req.get(API_URL+'users/{}/todos'.format(user_id))
        user_todos = res.json()
        response_dict[user_id] = [{'username': user.get('username'),
                                   'task': todo.get('title'),
                                   'completed': todo.get('completed')}
                                  for todo in user_todos]
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(response_dict, jsonfile)
