"""
shift function
"""
import argparse
import sys
import os
from source import str_to_source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='shift function')

    if os.isatty(0):
        parser.add_argument('source', type=str_to_source)
    else:
        cmd = sys.stdin.read()
        parser.add_argument('-source', '--source',
                            type=str_to_source,
                            default=str_to_source(cmd)
                            )

    parser.add_argument('args', type=float, nargs='*')

    parser.add_argument('-r', '--r', type=float)
    parser.add_argument('-g', '--g', type=float)
    parser.add_argument('-b', '--b', type=float)
    parser.add_argument('-a', '--a', type=float)

    args = parser.parse_args()

    source = args.source

    effect_args = {
            "r": 1,
            "g": 1,
            "b": 1,
            "a": 1,
            }

    # from positional args
    if len(args.args) > 0:
        effect_args["r"] = args.args[0]

    if len(args.args) > 1:
        effect_args["g"] = args.args[1]

    if len(args.args) > 2:
        effect_args["b"] = args.args[2]

    if len(args.args) > 3:
        effect_args["a"] = args.args[3]

    # from optional args
    if args.r is not None:
        effect_args["r"] = args.r

    if args.g is not None:
        effect_args["g"] = args.g

    if args.b is not None:
        effect_args["b"] = args.b

    if args.a is not None:
        effect_args["a"] = args.a

    arg_list = [
            effect_args["r"],
            effect_args["g"],
            effect_args["b"],
            effect_args["a"],
            ]

    source.add_effect("shift", arg_list)

    print(str(source))
