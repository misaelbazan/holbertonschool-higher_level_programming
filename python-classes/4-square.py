#!/usr/bin/python3
"""This modules defines a square"""


class Square:
    """This class builds an object from type(Square)"""

    def __init__(self, size=0):
        """This function initializes a new object from Square class"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """size attribute getter, that returns size"""
        return(self.__size)

    @size.setter
    def size(self, new_size):
        """size attribute setter
        Args:
            new_size: its value will be set as size if passes all conditions"""
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

    def area(self):
        """returns the area of the square, and uses size attribute"""
        return self.__size * self.__size
