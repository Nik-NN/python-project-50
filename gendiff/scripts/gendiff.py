import argparse


def main():
      parser = argparse.ArgumentParser(prog ='gendiff', description ='Compares two configuration files and shows a difference.')
      parser.add_argument('-f', '--format', help='set format of output')
      parser.add_argument('first_file')
      parser.add_argument('second_file')
      args = parser.parse_args()
      print(args)

if __name__ == '__main__':
	main()
