#!/usr/bin/python3
''' How many subs? '''
import requests


def top_ten(subreddit):
    ''' returns the number of subscribers '''
    URL = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Diego'}
    reqJson = requests.get(URL, headers=headers, allow_redirects=False)
    if reqJson.status_code == 200:
        for reques in reqJson.json()['data']['children']:
            print(reques['data']['title'])
    else:
        print('None')
