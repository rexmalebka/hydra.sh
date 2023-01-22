"""
repeat function
"""
import argparse
import sys
import os
from source import str_to_source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='repeat function')

    if os.isatty(0):
        parser.add_argument('source', type=str_to_source)
    else:
        cmd = sys.stdin.read()
        parser.add_argument('-source', '--source',
                            type=str_to_source,
                            default=str_to_source(cmd)
                            )

    parser.add_argument('args', type=float, nargs='*')

    parser.add_argument('-repeatX', '--repeatX', type=float)
    parser.add_argument('-repeatY', '--repeatY', type=float)
    parser.add_argument('-offsetX', '--offsetX', type=float)
    parser.add_argument('-offsetY', '--offsetY', type=float)

    args = parser.parse_args()

    source = args.source

    effect_args = {
            "repeatX": 3.0,
            "repeatY": 3.0,
            "offsetX": 0.0,
            "offsetY": 0.0,
            }

    # from positional args
    if len(args.args) > 0:
        effect_args["repeatX"] = args.args[0]

    if len(args.args) > 1:
        effect_args["repeatY"] = args.args[1]

    if len(args.args) > 2:
        effect_args["offsetX"] = args.args[2]

    if len(args.args) > 3:
        effect_args["offsetY"] = args.args[3]

    # from optional args
    if args.repeatX is not None:
        effect_args["repeatX"] = args.repeatX

    if args.repeatY is not None:
        effect_args["repeatY"] = args.repeatY

    if args.offsetX is not None:
        effect_args["offsetX"] = args.offsetX

    if args.offsetY is not None:
        effect_args["offsetY"] = args.offsetY

    arg_list = [
            effect_args["repeatX"],
            effect_args["repeatY"],
            effect_args["offsetX"],
            effect_args["offsetY"],
            ]

    source.add_effect("repeat", arg_list)

    print(str(source))
