#!/usr/bin/python3
"""This module contains:
    Methods: 1
        is_same_class(obj, a_class): Returns true if the object is \
                exactyly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """This method evaluates if an object is an instance of a specified class
    Return:
        True: if obj is exactly an instance of the specified class
        False: otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False
