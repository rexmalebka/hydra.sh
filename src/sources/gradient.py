"""
gradient source
"""
import argparse
from source import Source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='gradient source')
    parser.add_argument('args', type=float, nargs='*')

    parser.add_argument('-speed', '--speed', type=float)

    # frequency: 60, sync: 0.1, offset
    args = parser.parse_args()

    osc_args = {
            "speed": 0
            }

    if len(args.args) > 0:
        osc_args["speed"] = args.args[0]

    # from optional args
    if args.speed is not None:
        osc_args["speed"] = args.speed

    arg_list = [
            osc_args["speed"]
            ]

    src = Source("gradient", arg_list)

    print(src)
