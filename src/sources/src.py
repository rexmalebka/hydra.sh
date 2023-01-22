"""
src source
"""
import argparse
from source import Source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='src source')
    parser.add_argument(
            'input',
            type=str,
            default='o0',
            choices=[
                'o0', 'o1', 'o2', 'o3',
                's0', 's1', 's2', 's3'
                ])

    # frequency: 60, sync: 0.1, offset
    args = parser.parse_args()

    src = Source('src', [args.input])

    print(src)
