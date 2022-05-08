# CLI (command-line interface)
from argparse import ArgumentParser

args = ArgumentParser()

args.add_argument("first_arg")
args.add_argument("value")

args = vars(args.parse_args())

print(f"Hello {args['first_arg']}! My value is {args['value']}")