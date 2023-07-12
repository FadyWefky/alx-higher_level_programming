#!/usr/bin/python3
"""Write a class MyList that inherits from list"""


class MyList(list):
    """MyList class heredit from list base class"""
    def print_sorted(self):
        """Print a sorted list"""
        print(sorted(self))
