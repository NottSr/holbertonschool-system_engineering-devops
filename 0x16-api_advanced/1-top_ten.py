#!/usr/bin/python3
"""
Function that queries the Reddit API and
prints the titles of the first 10 hot posts
"""

import requests


def top_ten(subreddit):

    burl = "https://www.reddit.com"
    aurl = "{}/r/{}/hot.json".format(burl, subreddit)

    usag = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/105.0.0.0 Safari/537.36'
    }

    res = requests.get(
        aurl,
        headers=usag,
        params={'limit': 10},
        allow_redirects=False
    )

    if res.status_code in [302, 404]:
        print(None)
    else:
        for pt in res.json()['data']['children']:
            print(pt['data']['title'])
