"""
scale function
"""
import argparse
import sys
import os
from source import str_to_source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='scale function')

    if os.isatty(0):
        parser.add_argument('source', type=str_to_source)
    else:
        cmd = sys.stdin.read()
        parser.add_argument('-source', '--source',
                            type=str_to_source,
                            default=str_to_source(cmd)
                            )

    parser.add_argument('args', type=float, nargs='*')

    parser.add_argument('-amount', '--amount', type=float)
    parser.add_argument('-xMult', '--xMult', type=float)
    parser.add_argument('-yMult', '--yMult', type=float)
    parser.add_argument('-offsetX', '--offsetX', type=float)
    parser.add_argument('-offsetY', '--offsetY', type=float)

    # amount: 1.5, xMult: 1, yMult: 1, offsetX: 0.5, offsetY: 0.5
    args = parser.parse_args()

    source = args.source

    effect_args = {
            "amount": 1.5,
            "xMult": 1,
            "yMult": 1,
            "offsetX": 0.5,
            "offsetY": 0.5,
            }

    # from positional args
    if len(args.args) > 0:
        effect_args["amount"] = args.args[0]

    if len(args.args) > 1:
        effect_args["xMult"] = args.args[1]

    if len(args.args) > 2:
        effect_args["yMult"] = args.args[2]

    if len(args.args) > 3:
        effect_args["offsetX"] = args.args[3]

    if len(args.args) > 4:
        effect_args["offsetY"] = args.args[4]

    # from optional args
    if args.amount is not None:
        effect_args["amount"] = args.amount

    if args.xMult is not None:
        effect_args["xMult"] = args.xMult

    if args.yMult is not None:
        effect_args["yMult"] = args.yMult

    if args.offsetX is not None:
        effect_args["offsetX"] = args.offsetX

    if args.offsetY is not None:
        effect_args["offsetY"] = args.offsetY

    arg_list = [
            effect_args["amount"],
            effect_args["xMult"],
            effect_args["yMult"],
            effect_args["offsetX"],
            effect_args["offsetY"],
            ]

    source.add_effect("scale", arg_list)

    print(str(source))
