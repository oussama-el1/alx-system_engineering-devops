#!/usr/bin/python3
"""
script that return information about todos for rmployer
"""
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    employer = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    todo_list = requests.get(url + "todos",
                             params={"userId": sys.argv[1]}).json()
    complited = []
    for task in todo_list:
        if task.get('completed') is True:
            complited.append(task)
    print('Employee {} is done with tasks({}/{}):'
          .format(employer.get('name'), len(complited), len(todo_list)))
    for task in complited:
        print("\t {}".format(task.get('title')))
