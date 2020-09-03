"""
in a loop

Enter a URL 
shows the data of the url

caches the data so subsequen requests for the same ULR return the cache data. Instead of going over the network again

Stuff to figure out
* How to get data froma URL
* How are going to cache it
* what happens if the server gets updated

"""
import urllib.request
import datetime

class CacheEntry:
    def __init__(self, data):
        self.data = data
        self.timestamp = datetime.datetime.now().timestamp()
        
MAX_AGE = 10  # seconds

cache = {}

while True:
    url = input("Enter a url: ")

    cur_time = datetime.datetime.now().timestamp()

    if url not in cache or cur_time - cache[url].timestamp > MAX_AGE:
        print("CACHE MISS")
          
        with urllib.request.urlopen(url) as response:
            data = response.read()

        cache[url] = CacheEntry(data)    
    else:
        print("CACHE HIT")

    print(cache[url].data[:65])