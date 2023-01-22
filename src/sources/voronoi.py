"""
voronoi source
"""
import argparse
from source import Source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='voronoi source')
    parser.add_argument('args', type=float, nargs='*')

    parser.add_argument('-scale', '--scale', type=float)
    parser.add_argument('-speed', '--speed', type=float)
    parser.add_argument('-blending', '--blending', type=float)

    # scale: 60, speed: 0.1, blending
    args = parser.parse_args()

    osc_args = {
            "scale": 5,
            "speed": 0.3,
            "blending": 0.3
            }

    if len(args.args) > 0:
        osc_args["scale"] = args.args[0]

    if len(args.args) > 1:
        osc_args["speed"] = args.args[1]

    if len(args.args) > 2:
        osc_args["blending"] = args.args[2]

    # from optional args
    if args.scale is not None:
        osc_args["scale"] = args.scale

    if args.speed is not None:
        osc_args["speed"] = args.speed

    if args.blending is not None:
        osc_args["blending"] = args.blending

    arg_list = [
            osc_args["scale"],
            osc_args["speed"],
            osc_args["blending"]
            ]

    src = Source("voronoi", arg_list)

    print(src)
