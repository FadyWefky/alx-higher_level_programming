#!/usr/bin/python3
"""Number of lines"""


def number_of_lines(filename=""):
    """Number of lines"""
    with open(filename, mode='r', encoding='utf-8') as my_file:
        count_line = 0

        for line in my_file:
            count_line += 1
        return count_line
