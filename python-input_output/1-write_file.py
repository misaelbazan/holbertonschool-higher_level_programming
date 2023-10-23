#!/usr/bin/python3
"""
This module contains 01 functions:
    1. write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """This function writes a string to a text file
    Args:
        filename: name of the file to be written
        text: string to write to filename
    Return:
        The number of the characters written
    """
    with open(filename, 'w') as file:
        """Open the file in write mode"""
        file.write(text)

    return len(text)
