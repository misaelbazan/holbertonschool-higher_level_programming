#!/usr/bin/python3
"""
This module contains:
    01 functions:
    1. read-file()
"""


def read_file(filename=""):
    """This function reads a text file and prints it to sdtout
    Args:
        filename: the text file to read and print its content to stdout
    Return:
        Nothing
    """
    with open(filename, 'r') as file:
        """Open the file in read mode"""

        content = file.read()   # Read the entire content of the file

    print(content, end="")   # Print or use the content as needed
