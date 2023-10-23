#!/usr/bin/python3
"""
This module contains 01 functions:
    1. append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """This function appends a string the end of a text file
    Args:
        filename: file to append the text
        text: text to be appended to the file
    Return:
        The number of characters added
    """
    with open(filename, 'a') as file:
        """Opend the file in append mode"""
        file.write(text)
        """Append content to the file"""

    return len(text)
