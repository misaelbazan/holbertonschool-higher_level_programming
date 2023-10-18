#!/usr/bin/python3
"""This module contains:
    Methods: 1
        is_same_class(obj, a_class): Returns true if the object is \
                exactyly an instance of the specified class
"""


def is_same_class(obj, a_class):
    if isinstance(obj, a_class) and type(obj) == a_class:
        return True
    else:
        return False
