#!/usr/bin/python3
"""This modules defines a square"""


class Square:
    """This class builds an object from type(Square)"""

    def __init__(self, size=0):
        """
        This function initializes a new object from Square class
        Args:
            size: is the side longitude of the square obj"
        """

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
    def size(self, value):
        """size attribute setter
        Args:
            new_size: its value will be set as size if passes all conditions"""
        if not isinstance(value, int) or not isinstance(value, float):
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

    def area(self):
        """returns the area of the square, and uses size attribute"""
        return self.__size * self.__size

    def __eq__(self, other):
        """Checks if two esquare have equal areas"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if two squares have different areas"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if the area of one square is greater than another"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if the area of one square is greater
        than or equal to another square area"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Checks if the area of one square is smaller than another"""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if the area of one square is smaller
        than or equal to another square are"""
        return self.area() <= other.area()
