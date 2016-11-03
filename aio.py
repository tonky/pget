#!/usr/local/bin/python3.5
import time
import asyncio
from aiohttp import ClientSession

start = time.time()

async def fetch(url, session):
    async with session.get(url) as response:
        print("'%s\' fetched in %ss" % (url, (time.time() - start)))
        return await response.read()

async def run(loop,  r):
    url = "http://localhost:8080/{}"
    tasks = []

    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(fetch(url.format(i), session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        print("Elapsed Time: %s" % (time.time() - start))
        # you now have all response bodies in this variable
        # print(responses)

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(loop, 1000))
loop.run_until_complete(future)
