#!/usr/bin/python3
'''using this REST API, for a given employee ID, returns information\
about his/her TODO list progress'''
import requests
from sys import argv

if __name__ == "__main__":
    csv = ""
    html = "https://jsonplaceholder.typicode.com/"
    users = requests.get("{}users/{}".format(html, argv[1]))
    json_usr = users.json()
    todos = requests.get("{}todos".format(html))
    json_tds = todos.json()
    for dic in json_tds:
        if dic['userId'] == int(argv[1]):
            csv += '"{}","{}","{}","{}"\n'.format(argv[1],
                                                  json_usr['username'],
                                                  dic['completed'],
                                                  dic['title'])
    with open(argv[1]+".csv", "w+") as file:
        file.write(csv)
