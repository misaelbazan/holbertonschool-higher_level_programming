#!/usr/bin/python3
"""This module contains 01 functions"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters:
        ., ?, :
    """
    text = " ".join(text.split())
    chars = [".", "?", ":"]
    result = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        result += char
        if char in chars:
            result += "\n\n"
    bresult = [line.lstrip() for line in result.split('\n')]
    formated_txt = '\n'.join(bresult)
    print(formated_txt)
