Start webserver on localhost:8080

Make it answer queries on /<str: name>
Response should be "Hi there, I love %s!" % name
Each request has a delay of 100ms to simulate network connection


Server start
============
Python: python srv.py
Go:		./srv


Bench runs
==========
Python: python [aio.py,threads.py,procs.py]
Go:		./srv bench 1000


Results
=======

aiohttp webserver
-----------------
aio.py = 5.9s
threads.py = 1.8s
procs.py = 2.4s


go webserver
------------
aio.py = 5.7s
threads.py = 0.7s
procs.py = 1.8s
srv bench 1000 = 0.3s
