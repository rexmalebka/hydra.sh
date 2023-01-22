"""
rotate function
"""
import argparse
import sys
import os
from source import str_to_source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='rotate function')

    if os.isatty(0):
        parser.add_argument('source', type=str_to_source)
    else:
        cmd = sys.stdin.read()
        parser.add_argument('-source', '--source',
                            type=str_to_source,
                            default=str_to_source(cmd)
                            )

    parser.add_argument('args', type=float, nargs='*')

    parser.add_argument('-angle', '--angle', type=float)
    parser.add_argument('-speed', '--speed', type=float)

    args = parser.parse_args()

    source = args.source

    effect_args = {
            "angle": 10.0,
            "speed": 0.0,
            }

    # from positional args
    if len(args.args) > 0:
        effect_args["angle"] = args.args[0]

    if len(args.args) > 1:
        effect_args["speed"] = args.args[1]

    # from optional args
    if args.angle is not None:
        effect_args["angle"] = args.angle

    if args.speed is not None:
        effect_args["speed"] = args.speed

    arg_list = [
            effect_args["angle"],
            effect_args["speed"],
            ]

    source.add_effect("rotate", arg_list)

    print(str(source))
