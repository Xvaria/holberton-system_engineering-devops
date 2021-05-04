#!/usr/bin/python3
'''using this REST API, for a given employee ID, returns information\
about his/her TODO list progress'''
import json
import requests
from sys import argv

if __name__ == "__main__":
    jsonf = {}
    json_dict = {}
    dicl = []
    html = "https://jsonplaceholder.typicode.com/"
    users = requests.get("{}users/{}".format(html, argv[1]))
    json_usr = users.json()
    todos = requests.get("{}todos".format(html))
    json_tds = todos.json()
    for dic in json_tds:
        if dic['userId'] == int(argv[1]):
            json_dict['task'] = dic['title']
            json_dict['completed'] = dic['completed']
            json_dict['username'] = json_usr['username']
            dicl.append(json_dict)
            json_dict = {}
    jsonf[argv[1]] = dicl
    with open(argv[1]+".json", "w") as file:
        json.dump(jsonf, file)
