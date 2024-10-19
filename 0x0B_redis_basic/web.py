#!/usr/bin/env python3
"""
web cache and tracker
"""
import requests
import redis
from functools import wraps

store = redis.Redis()

def count_url_access(method):
    """ Decorator counting how many times a URL is accessed """
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        
        # Debugging: Check what is stored in the cache
        if cached_data:
            print(f"[INFO] Cached data for {url}: {cached_data[:100]}")  # Show first 100 chars
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)
        
        # Debugging: Verify if HTML is fetched correctly
        print(f"[INFO] Fetched HTML for {url}: {html[:100]}")  # Show first 100 chars

        store.incr(count_key)
        store.set(cached_key, html)
        store.expire(cached_key, 10)  # Cache expires after 10 seconds
        
        # Debugging: Verify the increment and set commands
        count_value = store.get(count_key)
        print(f"[INFO] URL access count for {url}: {count_value.decode('utf-8')}")
        
        return html
    return wrapper

@count_url_access
def get_page(url: str) -> str:
    """ Returns HTML content of a url """
    res = requests.get(url)
    
    # Debugging: Verify the status of the request
    print(f"[INFO] Request status for {url}: {res.status_code}")
    
    return res.text

# Example usage:
url = "http://google.com"
page_content = get_page(url)
