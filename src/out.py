"""
out function
"""
import argparse
import sys
import os
import asyncio
from source import str_to_source

from aiohttp import ClientSession, ClientWebSocketResponse
from aiohttp.http_websocket import WSMessage


def parse_args(args):
    script = ""
    for arg in args:
        if type(arg) in [int, float] :
            script += f'{arg},'

    script = script[:-1]
    return script

def parse_effects(effects):
    script = ""

    for effect in effects:
        name = effect['name'] 
        args_script = parse_args(effect['args'])
        script += f".{name}({args_script})"
    return script

def parse(source, buffer):
    args = parse_args(source.args)
    effects = parse_effects(source.effects)

    script = f"{source.name}({args})"
    script += f"{effects}"
    script += f'.out({buffer})'

    return script

async def send_script(websocket, script):
    await websocket.send_json({
        "script": script
        })


async def main(script):
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = os.environ.get('PORT', '8080')

    async with ClientSession() as session:
        async with session.ws_connect(
                f"http://{HOST}:{PORT}/bash",
                ssl=False) as ws:
            send_message_task = asyncio.create_task(
                    send_script(
                        websocket=ws,
                        script=script
                        )
                    )

            done, pending = await asyncio.wait(
                    [send_message_task],
                    return_when=asyncio.FIRST_COMPLETED,
                    )

            # First, we want to close the websocket connection
            if not ws.closed:
                await ws.close()

            # Then, we cancel each task which is pending:
            for task in pending:
                task.cancel()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='out function')

    if os.isatty(0):
        parser.add_argument('source', type=str_to_source)
    else:
        cmd = sys.stdin.read()
        parser.add_argument('-source', '--source',
                            type=str_to_source,
                            default=str_to_source(cmd)
                            )

    parser.add_argument(
            'buffer',
            type=str,
            default='o0',
            choices=[
                'o0', 'o1', 'o2', 'o3',
                's0', 's1', 's2', 's3'
                ],
            nargs='?'
            )
    args = parser.parse_args()
    print(parse(args.source, args.buffer))
    script = parse(
            args.source,
            args.buffer
            )
    asyncio.run(main(script))
