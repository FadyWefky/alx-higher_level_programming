#!/usr/bin/python3
"""Inherit from"""


def inherits_from(obj, a_class):
    """Return true if is decend and False if no"""
    return isinstance(obj, a_class) and not type(obj) == a_class
