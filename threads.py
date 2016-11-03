import threading
from urllib.request import urlopen
import time

start = time.time()

url = "http://localhost:8080/{}"
urls = []

def fetch_url(url):
    urlHandler = urlopen(url)
    html = urlHandler.read()
    print("'%s\' fetched in %ss" % (url, (time.time() - start)))
    return html

for i in range(1000):
    urls.append(url.format(i))

threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Elapsed Time: %s" % (time.time() - start))
