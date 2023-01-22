"""
kaleid function
"""
import argparse
import sys
import os
from source import str_to_source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='kaleid function')

    if os.isatty(0):
        parser.add_argument('source', type=str_to_source)
    else:
        cmd = sys.stdin.read()
        parser.add_argument('-source', '--source',
                            type=str_to_source,
                            default=str_to_source(cmd)
                            )

    parser.add_argument('args', type=float, nargs='*')

    parser.add_argument('-nSides', '--nSides', type=float)

    # nSides: 4.0
    args = parser.parse_args()

    source = args.source

    effect_args = {
            "nSides": 4.0,
            }

    # from positional args
    if len(args.args) > 0:
        effect_args["nSides"] = args.args[0]

    # from optional args
    if args.nSides is not None:
        effect_args["nSides"] = args.nSides

    arg_list = [
            effect_args["nSides"],
            ]

    source.add_effect("kaleid", arg_list)

    print(str(source))
