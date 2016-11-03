from aiohttp import web
import asyncio

async def handle(request):
    await asyncio.sleep(0.1)

    name = request.match_info.get('name', "Anonymous")
    text = "Hi there, I love %s!" % name
    return web.Response(text=text)

app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)

web.run_app(app)
