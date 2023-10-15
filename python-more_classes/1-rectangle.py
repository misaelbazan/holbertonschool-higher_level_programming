#!/usr/bin/python3
"""Class Rectangle:
    Define a rectangle
"""


class Rectangle:
    """
    This class defines a Rectangle Obj
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        """Initialize a new instance of Rectangle
        Args:
            width: the the width of the rectangle
            height: the height of the rectangle
        """

    @property
    def width(self):
        """Returns the actual width of the Obj"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width value from the outside"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height value from the outside"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
