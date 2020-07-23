#!/usr/bin/env python3

"""wcat = wc + cat combine"""


import sys


ENCODING = 'utf-8'

HELP_MESSAGE = __doc__ + """

Допускаются следующие режимы работы:
•	-h или --help - вывести справку о программе и завершить работу
•	-l или --lines - вывести количество строк в файле
•	-с или --chars - вывести количество символов в файле
•	-m или --max - вывести максимальную длину строки"""

HELP_MODES = ['-h', '--help']
COUNT_MODES = ['-l', '--lines']
LENGTH_MODES = ['-c', '--chars']
MAX_MODES = ['-m', '--max']
AVAILABLE_PARAMETERS = COUNT_MODES + LENGTH_MODES + MAX_MODES


def main():
    if len(sys.argv) == 1:
        print(HELP_MESSAGE)
        exit(-1)

    mode_parameter = sys.argv[1]

    if mode_parameter in HELP_MODES:
        print(HELP_MESSAGE)
        exit(0)

    if len(sys.argv) != 3:
        print(HELP_MESSAGE)
        exit(-1)

    if mode_parameter not in AVAILABLE_PARAMETERS:
        print(HELP_MESSAGE)
        exit(-1)

    input_file_path = sys.argv[2]

    count_lines = 0
    file_char_length = 0
    max_length = 0

    with open(input_file_path, 'r', encoding=ENCODING) as input_file:
        for line in input_file:
            count_lines += 1
            line = line.rstrip('\n')
            line_length = len(line)
            file_char_length += line_length
            max_length = max(max_length, line_length)
            print(line)


    print()

    if mode_parameter in COUNT_MODES:
        print(count_lines)

    elif mode_parameter in LENGTH_MODES:
        print(file_char_length)

    elif mode_parameter in MAX_MODES:
        print(max_length)


if __name__ == '__main__':
    main()
