"""
solid source
"""
import argparse
from source import Source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='solid source')
    parser.add_argument('args', type=float, nargs='*')

    parser.add_argument('-r', '--r', type=float)
    parser.add_argument('-g', '--g', type=float)
    parser.add_argument('-b', '--b', type=float)
    parser.add_argument('-a', '--a', type=float)

    # frequency: 60, sync: 0.1, offset
    args = parser.parse_args()

    osc_args = {
            "r": 0.0,
            "g": 0.0,
            "b": 0.0,
            "a": 0.0,
            }

    if len(args.args) > 0:
        osc_args["r"] = args.args[0]

    if len(args.args) > 1:
        osc_args["g"] = args.args[1]

    if len(args.args) > 2:
        osc_args["b"] = args.args[2]

    if len(args.args) > 3:
        osc_args["a"] = args.args[3]

    # from optional args
    if args.r is not None:
        osc_args["r"] = args.r

    if args.g is not None:
        osc_args["g"] = args.g

    if args.b is not None:
        osc_args["b"] = args.b

    if args.a is not None:
        osc_args["a"] = args.a

    arg_list = [
            osc_args["r"],
            osc_args["g"],
            osc_args["b"],
            osc_args["a"],
            ]

    src = Source("solid", arg_list)

    print(src)
