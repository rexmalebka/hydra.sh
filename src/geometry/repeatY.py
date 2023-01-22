"""
repeatY function
"""
import argparse
import sys
import os
from source import str_to_source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='repeatY function')

    if os.isatty(0):
        parser.add_argument('source', type=str_to_source)
    else:
        cmd = sys.stdin.read()
        parser.add_argument('-source', '--source',
                            type=str_to_source,
                            default=str_to_source(cmd)
                            )

    parser.add_argument('args', type=float, nargs='*')

    parser.add_argument('-reps', '--reps', type=float)
    parser.add_argument('-offset', '--offset', type=float)

    args = parser.parse_args()

    source = args.source

    effect_args = {
            "reps": 3.0,
            "offset": 0.0,
            }

    # from positional args
    if len(args.args) > 0:
        effect_args["reps"] = args.args[0]

    if len(args.args) > 1:
        effect_args["offset"] = args.args[1]

    # from optional args
    if args.reps is not None:
        effect_args["reps"] = args.reps

    if args.offset is not None:
        effect_args["offset"] = args.offset

    arg_list = [
            effect_args["reps"],
            effect_args["offset"],
            ]

    source.add_effect("repeatY", arg_list)

    print(str(source))
