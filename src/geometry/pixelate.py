"""
pixelate function
"""
import argparse
import sys
import os
from source import str_to_source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='pixelate function')

    if os.isatty(0):
        parser.add_argument('source', type=str_to_source)
    else:
        cmd = sys.stdin.read()
        parser.add_argument('-source', '--source',
                            type=str_to_source,
                            default=str_to_source(cmd)
                            )

    parser.add_argument('args', type=float, nargs='*')

    parser.add_argument('-x', '--x', type=float)
    parser.add_argument('-y', '--y', type=float)

    # x: 20.0, y: 20.0
    args = parser.parse_args()

    source = args.source

    effect_args = {
            "x": 20.0,
            "y": 20.0,
            }

    # from positional args
    if len(args.args) > 0:
        effect_args["x"] = args.args[0]

    if len(args.args) > 1:
        effect_args["y"] = args.args[1]

    # from optional args
    if args.x is not None:
        effect_args["x"] = args.x

    if args.y is not None:
        effect_args["y"] = args.y

    arg_list = [
            effect_args["x"],
            effect_args["y"],
            ]

    source.add_effect("pixelate", arg_list)

    print(str(source))
