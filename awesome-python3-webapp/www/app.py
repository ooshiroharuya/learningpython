#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ooshiroharuya
@software: PyCharm
@file: app.py.py
@time: 2022/3/22 00:28
"""
import asyncio
import logging; logging.basicConfig(level=logging.INFO)

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', headers={'content-type':'text/html'})

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
