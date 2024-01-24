#!/usr/bin/env python3
"""Cache number of requests"""


import requests
import redis


def get_page(url: str) -> str:
    """
    get_page - Fetch pages from a url
    @url: Url to fetch from
    Returns: String
    """
    redis_instance = redis.Redis()
    contents = requests.get(url).text
    r.setex(url, 10, contents)
    r.incr('count' + ':' + url)
