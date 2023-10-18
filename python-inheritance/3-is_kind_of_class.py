#!/usr/bin/python3
"""This module contains:
    Methods: 1
        is_kind_of_class: Returns True or False
"""


def is_kind_of_class(obj, a_class):
    """This method evaluates if an object is an instance of a specified class
    Return:
        True: if obj is an instance of the specified class
        False: otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
