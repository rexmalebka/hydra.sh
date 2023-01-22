"""
posterize function
"""
import argparse
import sys
import os
from source import str_to_source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='posterize function')

    if os.isatty(0):
        parser.add_argument('source', type=str_to_source)
    else:
        cmd = sys.stdin.read()
        parser.add_argument('-source', '--source',
                            type=str_to_source,
                            default=str_to_source(cmd)
                            )

    parser.add_argument('args', type=float, nargs='*')

    parser.add_argument('-bins', '--bins', type=float)
    parser.add_argument('-tolerance', '--tolerance', type=float)

    args = parser.parse_args()

    source = args.source

    effect_args = {
            "bins": 3,
            "tolerance": 0.1,
            }

    # from positional args
    if len(args.args) > 0:
        effect_args["bins"] = args.args[0]

    if len(args.args) > 1:
        effect_args["tolerance"] = args.args[1]

    # from optional args
    if args.bins is not None:
        effect_args["bins"] = args.bins

    if args.tolerance is not None:
        effect_args["tolerance"] = args.tolerance

    arg_list = [
            effect_args["bins"],
            effect_args["tolerance"],
            ]

    source.add_effect("posterize", arg_list)

    print(str(source))
