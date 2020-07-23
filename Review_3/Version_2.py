#!/usr/bin/env python3

"""usage: wg.py -d <dict_file_path>

Classic Last Letter Game. Every next word should starts from last letter of previous word.
No repeats are allowed."""


import argparse
import collections


ENCODING = 'utf-8'
DEFAULT_FILE_WITH_PROGRAM_WORD_LIST = 'wg.txt'


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('-d', default=DEFAULT_FILE_WITH_PROGRAM_WORD_LIST, help='input dictionary table file path')

    return parser.parse_args()


def program_turn(key_letter, dictionary):
    for words in dictionary[key_letter]:
        yield from dictionary[key_letter]


def main():
    options = parse_args()
    new_words = set()
    key_letter = None
    dictionary = collections.defaultdict(list)

    with open(options.d, 'r', encoding=ENCODING) as dict_table:
        program_word_list = set(line.strip().lower() for line in dict_table if line.strip())

    for word in program_word_list:
        dictionary[word[0]].append(word)

    print(dictionary)
    print()
    print('Please enter you first word.')

    try:
        while True:
            word = input().lower().strip()

            if key_letter and key_letter != word[0]:
                print("Wrong. Enter word starting with '{}'".format(key_letter))
                continue

            if word in new_words:
                print('Wrong. This word was already used. Please enter new word or press Ctrl+C to exit')
                continue

            key_letter = word[-1]
            new_words.add(word)

            while word in new_words:
                word = program_turn(key_letter, dictionary)

            print(word)
            key_letter = word[-1]
            new_words.add(word)
            print("Your turn. Enter word starting with '{}'".format(key_letter))

    except KeyboardInterrupt:
        print('YOU DIED!')
    finally:
        with open(options.d, 'w', encoding=ENCODING) as dict_table:
            for word in program_word_list:
                dict_table.print(word)
            for word in new_words:
                dict_table.print(word)


if __name__ == '__main__':
    main()
