"""
scrollY function
"""
import argparse
import sys
import os
from source import str_to_source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='scrollY function')

    if os.isatty(0):
        parser.add_argument('source', type=str_to_source)
    else:
        cmd = sys.stdin.read()
        parser.add_argument('-source', '--source',
                            type=str_to_source,
                            default=str_to_source(cmd)
                            )

    parser.add_argument('args', type=float, nargs='*')

    parser.add_argument('-scrollY', '--scrollY', type=float)
    parser.add_argument('-speed', '--speed', type=float)

    args = parser.parse_args()

    source = args.source

    effect_args = {
            "scrollY": 1.5,
            "speed": 1,
            }

    # from positional args
    if len(args.args) > 0:
        effect_args["scrollY"] = args.args[0]

    if len(args.args) > 1:
        effect_args["speed"] = args.args[1]

    # from optional args
    if args.scrollY is not None:
        effect_args["scrollY"] = args.scrollY

    if args.speed is not None:
        effect_args["speed"] = args.speed

    arg_list = [
            effect_args["scrollY"],
            effect_args["speed"],
            ]

    source.add_effect("scrollY", arg_list)

    print(str(source))
