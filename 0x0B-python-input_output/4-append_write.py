#!/usr/bin/python3
"""Append"""


def append_write(filename="", text=""):
    """Append"""
    with open(filename, mode='a', encoding='utf-8') as my_file:
        my_file.write(text)
        return (len(text))
