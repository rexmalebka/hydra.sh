"""
colorama function
"""
import argparse
import sys
import os
from source import str_to_source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='colorama function')

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

    args = parser.parse_args()

    source = args.source

    effect_args = {
            "amount": 0.4,
            }

    # from positional args
    if len(args.args) > 0:
        effect_args["amount"] = args.args[0]

    # from optional args
    if args.amount is not None:
        effect_args["amount"] = args.amount

    arg_list = [
            effect_args["amount"],
            ]

    source.add_effect("colorama", arg_list)

    print(str(source))
