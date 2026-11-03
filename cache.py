"""
constructed a function to look up the cache of a URL
if it exists it loads page
if not it makes the server do some work
"""


cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server()
        cache[url] = data
        return data

