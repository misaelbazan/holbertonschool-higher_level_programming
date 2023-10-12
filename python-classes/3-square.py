#!/usr/bin/python3
"""This module represents the Square class"""


class Square:
    """This class builds an square object"""

    def __init__(self, size=0):
        """Here a new object is initialized"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """This method takes the size of the square and returns the area"""

        square_area = self.__size * self.__size
        return square_area
