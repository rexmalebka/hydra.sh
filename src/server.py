"""
webserver and ws server
bash messages are sent to server and websocket server are sent to hydra
"""
import webbrowser
import os
import json
import aiohttp
from aiohttp import web


async def web_handler(request):
    """
    web handler for index.html
    """
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


async def ws_bash_handler(request):
    """
    web socket handler
    """
    ws_conn = web.WebSocketResponse(autoping=True, heartbeat=60)

    await ws_conn.prepare(request)

    async for msg in ws_conn:
        if msg.type == aiohttp.WSMsgType.TEXT:
            try:
                data = json.loads(msg.data)
                script = data.get("script", '')

                for conn in request.app['conn'].values():
                    await conn.send_json({
                        "script": script
                        })

            except json.decoder.JSONDecodeError:
                await ws_conn.close()
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print(f'ws connection closed with exception {ws_conn.exception()}')

    print('websocket connection closed')

    return ws_conn


async def ws_web_handler(request):
    """
    web socket handler
    """
    ws_conn = web.WebSocketResponse()
    await ws_conn.prepare(request)

    request.app['conn'][hash(ws_conn)] = ws_conn

    async for msg in ws_conn:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws_conn.close()
            else:
                print(msg.data)
                await ws_conn.send_str(msg.data + '/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print(f'ws connection closed with exception {ws_conn.exception()}')

    print('websocket connection closed')
    request.app['conn'].pop(hash(ws_conn))

    return ws_conn


if __name__ == '__main__':
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = os.environ.get('PORT', '8080')

    web_app = web.Application()
    web_app.add_routes([
        web.get('/ws', ws_web_handler),
        web.get('/bash', ws_bash_handler),
        web.static('/', "./static", show_index=True),
        ])

    web_app['conn'] = {}

    webbrowser.open(f"http://{HOST}:{PORT}/index.html")
    web.run_app(web_app, host=HOST, port=PORT)
