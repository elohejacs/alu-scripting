#!/usr/bin/python3
"""" Top Ten Limit"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-Reddit-Query"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return
    
    data = response.json().get("data", {}).get("children", [])
    for post in data:
        print(post.get("data", {}).get("title"))
