#!/usr/bin/python3
''' How many subs? '''
import requests


def number_of_subscribers(subreddit):
    ''' returns the number of subscribers '''
    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Diego'}
    reqJson = requests.get(URL, headers=headers, allow_redirects=False)
    if reqJson.status_code == 200:
        return (reqJson.json()['data']['subscribers'])
    else:
        return 0
