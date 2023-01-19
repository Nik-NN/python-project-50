#!/usr/bin/env python3
from gendiff.argparse import arg_parse
from gendiff.engine import generate_diff


def main():
    args = arg_parse()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
