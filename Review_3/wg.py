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


def end_program(dictionary, new_words, dictionary_path):
    print(dictionary)
    print(new_words)
    dictionary += new_words
    print(dictionary)
    with open(dictionary_path, 'w', encoding=ENCODING) as dict_table:
        for word in dictionary:
            dict_table.write(word)
            dict_table.write('\n')
    exit()


def main():
    options = parse_args()
    new_words = set()
    first_round = True
    program_lose = False

    with open(options.d, 'r', encoding=ENCODING) as dict_table:
        dictionary = sorted(frozenset(line.strip().lower() for line in dict_table if line.strip()),\
                            key=lambda el: el[0])

    dict_length = len(dictionary)

    try:
        while True:
            if program_lose:
                print('YOU WON!')
                break

            user_word = input().lower().strip()

            if first_round:
                key_letter = user_word[0]
                first_round = False

            if user_word in new_words or key_letter != user_word[0]:
                print('Incorrect. Please enter new word or press Ctrl+C to exit')
                continue

            key_letter = user_word[-1]
            new_words.add(user_word)
            index = 0

            for program_word in dictionary:
                index += 1
                if program_word[0] == key_letter and program_word not in new_words:
                    print(program_word)
                    key_letter = program_word[-1]
                    print("Your turn. Enter word starting with '{}'".format(key_letter))
                    new_words.add(program_word)
                    break
                elif index == dict_length:
                    program_lose = True

    except KeyboardInterrupt:
        print('YOU DIED!')
    finally:
        end_program(dictionary, new_words, options.d)


if __name__ == '__main__':
    main()
