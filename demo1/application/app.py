import logging; logging.basicConfig(level=logging.INFO)

import os
import json
import asyncio

from aiohttp import web

def index(request):
	resp = web.Response(body=b'<h1>what the hell fuck</h1>')
	resp.headers['content-type'] = 'text/html'
	return resp

async def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET', '/', index)
	server = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
	logging.info('server started at http://127.0.0.1:9000')
	return server

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()