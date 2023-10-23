#!/usr/bin/python3
"""
This module contains 01 functions:
    1. to_json_string(my_obj)
"""


import json
"""Importing json library"""


def to_json_string(my_obj):
    """This function returns the JSON representation of an object (string)
    Args:
        my_obj: the object to be converted to JSON representation
    Return:
        The JSON representation of <my_obj>
    """
    return json.dumps(my_obj)
