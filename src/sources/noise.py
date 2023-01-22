"""
noise source
"""
import argparse
from source import Source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='noise source')
    parser.add_argument('args', type=float, nargs='*')

    parser.add_argument('-scale', '--scale', type=float)
    parser.add_argument('-offset', '--offset', type=float)

    # scale: 10, offset: 0.1
    args = parser.parse_args()

    osc_args = {
            "scale": 10,
            "offset": 0.1
            }

    if len(args.args) > 0:
        osc_args["scale"] = args.args[0]

    if len(args.args) > 1:
        osc_args["offset"] = args.args[1]

    if args.scale is not None:
        osc_args["scale"] = args.scale

    if args.offset is not None:
        osc_args["offset"] = args.offset

    arg_list = [
            osc_args["scale"],
            osc_args["offset"]
            ]

    src = Source("noise", arg_list)

    print(src)
