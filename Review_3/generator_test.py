#!/usr/bin/env python3

"""usage: wg.py -d <dict_file_path>

Classic Last Letter Game. Every next word should starts from last letter of previous word.
No repeats are allowed."""

import argparse

ENCODING = 'utf-8'


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('-d', help='input dictionary table', default='wg.txt')

    return parser.parse_args()


def main():
    options = parse_args()

    with open(options.d, 'r', encoding=ENCODING) as dict_table:
        dictionary = sorted(frozenset(line.rstrip().lower() for line in dict_table if line.strip()), \
                            key=lambda el: el[0])

    print(type(dictionary))
    print(dictionary)

    print(dictionary.startswith('t'))


#    def word_generator(condition):
#        next_massiv = dictionary[dictionary.find(condition):dictionary.rfind(condition)]
#        print(next_massiv)
#        yield from next_massiv

#    while True:
#        word_from_user = input()
#        print(list(word_generator(word_from_user)))



if __name__ == '__main__':
    main()
