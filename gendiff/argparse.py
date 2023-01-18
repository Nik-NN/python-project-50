import argparse

def arg_parse():
    parser = argparse.ArgumentParser(prog ='gendiff', description ='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', help='set format of output', default='plain')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    return args
