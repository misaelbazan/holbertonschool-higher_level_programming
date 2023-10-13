#!/usr/bin/python3
"""
This module contains (01) modules:
    1. add_integer: function that adds its parameters
    Returns: result of the addition
"""
def add_integer(a, b=98):
    """
    This function adds two integers
    """
    if a is None or type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
