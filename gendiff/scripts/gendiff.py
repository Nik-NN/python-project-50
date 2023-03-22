#!/usr/bin/env python3
from gendiff.argparse import arg_parse
from gendiff.gendiff import generate_diff


def main():
    args = arg_parse()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
