import argparse
import sys
import json

def source(name, args):
    output = {
            "type": "source",
            "name": name,
            "args":args
            }

    return json.dumps(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='osc source')
    parser.add_argument('args', type=float, nargs='*')
    
    parser.add_argument('--frequency', type=float)
    parser.add_argument('--sync', type=float)
    parser.add_argument('--offset', type=float)
    #frequency: 60, sync: 0.1, offset
    args = parser.parse_args()

    osc_args = {
            "frequency": 60,
            "sync": 0.1,
            "offset": 0
            }

    if len(args.args) > 0:
        osc_args["frequency"] =args.args[0]

    if len(args.args) > 1:
        osc_args["sync"] =args.args[1]

    if len(args.args) > 2:
        osc_args["offset"] =args.args[2]


    if args.frequency != None:
        osc_args["frequency"] = args.frequency 

    if args.sync != None:
        osc_args["sync"] = args.sync

    if args.offset != None:
        osc_args["offset"] = args.offset

    arg_list = [
            osc_args["frequency"],
            osc_args["sync"],
            osc_args["offset"] 
            ]

    output = source("osc", arg_list)

    if not sys.stdout.isatty():
        output = output.replace(' ', '\x01')
    print(output)
    
