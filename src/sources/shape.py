"""
shape source
"""
import argparse
from source import Source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='shape source')
    parser.add_argument('args', type=float, nargs='*')

    parser.add_argument('-sides', '--sides', type=float)
    parser.add_argument('-radius', '--radius', type=float)
    parser.add_argument('-smoothing', '--smoothing', type=float)

    # frequency: 60, sync: 0.1, offset
    args = parser.parse_args()

    osc_args = {
            "sides": 3.0,
            "radius": 0.3,
            "smoothing": 0.01
            }

    if len(args.args) > 0:
        osc_args["sides"] = args.args[0]

    if len(args.args) > 1:
        osc_args["radius"] = args.args[1]

    if len(args.args) > 2:
        osc_args["smoothing"] = args.args[2]

    # from optional args
    if args.frequency is not None:
        osc_args["sides"] = args.sides

    if args.sync is not None:
        osc_args["radius"] = args.radius

    if args.offset is not None:
        osc_args["smoothing"] = args.smoothing

    arg_list = [
            osc_args["sides"],
            osc_args["radius"],
            osc_args["smoothing"]
            ]

    src = Source("shape", arg_list)

    print(src)
