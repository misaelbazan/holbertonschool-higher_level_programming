#!/usr/bin/python3
"""This module contains:
    Methods:
        01. inherits_from(obj, a_class): returns True of False
"""


def inherits_from(obj, a_class):
    """This methos evaluates if an instance is inherited from a specified class
    Args:
        obj: object to evaluate if inherits from a_class
        a_class: class that inherits to obj
    Return:
        True: if obj inherits directly or indirectly from a_class
        False: Otherwise
    """
    if isinstance(obj, a_class) and not type(obj) == a_class:
        return True
    else:
        return False
