#!/usr/bin/python3
"""
Function that queries the Reddit API and
returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):

    burl = "https://www.reddit.com"
    aurl = "{}/r/{}/about.json".format(burl, subreddit)

    usag = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/105.0.0.0 Safari/537.36'
    }

    res = requests.get(
        aurl,
        headers=usag,
        allow_redirects=False
    )

    if res.status_code in [302, 404]:
        return 0

    return res.json().get('data').get('subscribers')
