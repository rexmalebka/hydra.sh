"""
webserver and ws server
bash messages are sent to server and websocket server are sent to hydra
"""
import aiohttp
from aiohttp import web
import webbrowser
import os
import json


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
    ws = web.WebSocketResponse(autoping=True, heartbeat=60)

    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            try: 
                data = json.loads(msg.data)
                script = data.get("script", '')

                print("AAAA", request.app['conn'])
                for conn in request.app['conn'].values():
                    await conn.send_json({
                        "script": script
                        })

            except json.decoder.JSONDecodeError:
                await ws.close()
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print(f'ws connection closed with exception {ws.exception()}')

    print('websocket connection closed')

    return ws

async def ws_web_handler(request):
    """
    web socket handler
    """
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    request.app['conn'][hash(ws)] = ws

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                print(msg.data)
                await ws.send_str(msg.data + '/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print(f'ws connection closed with exception {ws.exception()}')

    print('websocket connection closed')
    request.app['conn'].pop(hash(ws))

    return ws


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
