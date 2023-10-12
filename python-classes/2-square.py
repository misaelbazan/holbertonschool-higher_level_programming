#!/usr/bin/python3
"""This module represents the Square class"""

class Square:
    """This class defines a square"""

    def __init__(self, size=0):
        """Initialize an Object of the Square class
        Args:
            self: 
            size: 0 by default, must be an integer
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
