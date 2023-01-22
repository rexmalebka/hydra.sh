"""
out function
"""
import argparse
import sys
import os
import json
import asyncio
from aiohttp import ClientSession
from source import str_to_source, Source


def parse_args(source_args):
    """
    parses args from source, verifies that args are correct
    """
    script = ""
    for arg in source_args:
        if (
                type(arg) in [int, float] or
                arg in ('o0', 'o1', 'o2', 'o3', 's0', 's1', 's2', 's3')
                ):
            script += f'{arg},'
        elif type(arg) is str:
            try:
                json_arg = json.loads(arg)
            except json.decoder.JSONDecodeError:
                pass

    script = script[:-1]
    return script


def parse_effects(effects):
    """
    parses effects from a source,  generating js code
    """
    script = ""

    for effect in effects:
        name = effect['name']
        args_script = parse_args(effect['args'])
        script += f".{name}({args_script})"
    return script


def parse(source):
    """
    parses source into valid js code
    """
    source_args = parse_args(source.args)
    effects = parse_effects(source.effects)

    script = f"{source.name}({source_args})"
    script += f"{effects}"

    return script


async def send_script(websocket, script):
    """
    sends js code via websocket
    """
    await websocket.send_json({
        "script": script
        })


async def main(script):
    """
    main asyncio function
    """
    host = os.environ.get('HOST', '0.0.0.0')
    port = os.environ.get('PORT', '8080')

    async with ClientSession() as session:
        async with session.ws_connect(
                f"http://{host}:{port}/bash",
                ssl=False) as ws_conn:
            send_message_task = asyncio.create_task(
                    send_script(
                        websocket=ws_conn,
                        script=script
                        )
                    )

            _, pending = await asyncio.wait(
                    [send_message_task],
                    return_when=asyncio.FIRST_COMPLETED,
                    )

            # First, we want to close the websocket connection
            if not ws_conn.closed:
                await ws_conn.close()

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

    hydra_script = parse(
            args.source
            )
    hydra_script += f'.out({args.buffer})'

    asyncio.run(main(hydra_script))
