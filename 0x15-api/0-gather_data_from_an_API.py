#!/usr/bin/python3
'''using this REST API, for a given employee ID, returns information\
about his/her TODO list progress'''
import requests
from sys import argv

if __name__ == "__main__":
    done_task = 0
    total_task = 0
    html = "https://jsonplaceholder.typicode.com/"
    users = requests.get("{}users/{}".format(html, argv[1]))
    json_usr = users.json()
    todos = requests.get("{}todos".format(html))
    json_tds = todos.json()
    tasks_usr = []
    for dic in json_tds:
        if dic['userId'] == int(argv[1]):
            total_task += 1
            if dic['completed']:
                tasks_usr.append(dic['title'])
                done_task += 1
    print("Employe {} is done with tasks({}/{}):".format(json_usr['name'],
                                                         done_task,
                                                         total_task))
    for title_task in tasks_usr:
        print("\t {}".format(title_task))