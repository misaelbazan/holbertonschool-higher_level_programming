#!/usr/bin/python3
"""
This module contains:
"""


def lookup(obj):
    """This function returns a list
    Args:
        obj: object with attributes to return
    Return:
        list: of available attributes and method of an object
    """
    return(dir(obj))
