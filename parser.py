import argparse, os, sys


def get():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--command')
    parser.add_argument('-n', '--name')
    return parser.parse_args()
