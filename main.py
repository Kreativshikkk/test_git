import os
import parser
import sys


def first_command():
    return sys.version


def second_command(directory_name):
    os.mkdir(f'./{directory_name}')


def third_command():
    return os.listdir('..')


def main():
    args = parser.get()
    if args.command == '1':
        print(first_command())
    elif args.command == '2':
        second_command(args.name)
    elif args.command == '3':
        print(third_command())


if __name__ == '__main__':
    main()
