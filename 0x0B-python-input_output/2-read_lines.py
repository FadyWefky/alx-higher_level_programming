#!/usr/bin/python3
"""Read n lines"""


def read_lines(filename="", nb_lines=0):
    """Read n lines"""
    with open(filename, encoding='utf-8') as my_file:
        count_line = 0

        for line in my_file:
            count_line += 1
            if (nb_lines <= 0) or (nb_lines >= count_line):
                print(line, end='')
    my_file.close()
