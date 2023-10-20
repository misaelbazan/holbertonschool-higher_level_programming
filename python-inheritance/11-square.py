#!/usr/bin/python3
"""This module contains 01 class, and imports 01 class
"""


Rectangle = __import__('9-rectangle').Rectangle
"""Import Rectangle class from 9-rectangle.py and assign it to Rectangle"""


class Square(Rectangle):
    """This class inherits from Rectangle:
    Inherited methods:
        __init__(self, width, height): takes 2 arguments and assings to
            the new object
        Rectangle.area(self): return the area of the square
        integer_validation(self, name, value):
        Return:
            True if "value" argument is a positive integer, False otherwise
        __str__(self):
        Return:
            [Rectangle] <width>/<height>
    """
    def __init__(self, size):
        """Initialize a new instance from the class Square:
        Args:
            size: longitude of each side of the square
        """
        super().__init__(size, size)
        """Here the inherited init method is used, taking size twice"""
        super().integer_validator("size", size)
        """Rectangle.integer_validator is being used"""
        self.__size = size

    def __str__(self):
        """Return: [Square] <size>/<size>"""
        return f"[{__class__.__name__}] {self.__size}/{self.__size}"
