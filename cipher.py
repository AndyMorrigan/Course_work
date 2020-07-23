#!/usr/bin/env python3


"""usage: cipher.py [-h] [-r] table input output

Classical substitution cipher

Special thanks:
To my father for my brains, to my teacher Luka for the knowledge =P"""


import argparse


ENCODING = 'utf-8'
BUFFER_SIZE = 0x1000


def single_char_buffered_read(file):
    buffer = True
    while buffer:
        buffer = file.read(BUFFER_SIZE)
        for character in buffer:
            yield character


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('table', help='substitution mapping file')
    parser.add_argument('input', help='input text file')
    parser.add_argument('output', help='output text file')
    parser.add_argument('-r', '--reverse', dest='reverse', action='store_true', help='read mapping reversed way')

    return parser.parse_args()


def main():
    options = parse_args()

    with open(options.table, 'r', encoding=ENCODING) as table_file:
        dictionary = dict(line.rstrip().split('-') for line in table_file if line.strip())

    if options.reverse:
        dictionary = {value: key for key, value in dictionary.items()}

    with open(options.input, 'r', encoding=ENCODING) as input_file,\
            open(options.output, 'w', encoding=ENCODING) as output_file:
        for character in single_char_buffered_read(input_file):
            output_file.write(dictionary.get(character, character))


if __name__ == '__main__':
    main()

