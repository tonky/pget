from multiprocessing import Pool
from urllib.request import urlopen
import time

start = time.time()

url = "http://localhost:8080/{}"
urls = []

for i in range(1000):
    urls.append(url.format(i))

def fetch_url(url):
    urlHandler = urlopen(url)
    html = urlHandler.read()
    print("'%s\' fetched in %ss" % (url, (time.time() - start)))

with Pool(100) as p:
    p.map(fetch_url, urls)

print("Elapsed Time: %s" % (time.time() - start))
