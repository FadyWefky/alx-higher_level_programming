#!/usr/bin/python3
"""Write line"""


def write_file(filename="", text=""):
    """Write lines"""
    with open(filename, mode='w', encoding='utf-8') as my_file:
        return (my_file.write(text))
