"""
source utils
"""
import json
import sys


class Source:
    """
    Source class for __str__ and argparse validation
    """
    def __init__(self, name, args, effects=None):
        self.name = name
        self.args = args
        self.effects = [] if effects is None else effects

    def add_effect(self, name, args):
        """
        appends an effect to effect list
        """
        self.effects.append({
            "name": name,
            "args": args
            })

    def __str__(self):
        output = {
                "name": self.name,
                "args": self.args,
                "effects": self.effects
                }
        output = json.dumps(output)

        if not sys.stdout.isatty():
            output = output.replace(' ', '\x01')

        return output


def str_to_source(str_source):
    """
    Validation function for argparse
    """
    str_source = str_source.replace('\x01', ' ')
    json_source = json.loads(str_source)

    return Source(
            json_source['name'],
            json_source['args'],
            json_source['effects']
            )
