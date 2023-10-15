#!/usr/bin/python3
"""
This module contains (01) Classes:
    Rectangle: Defines a rectangle
"""


class Rectangle:
    """This class defines a rectangle object"""
    def __init__(self, width=0, height=0):
        """Initialize a new object from the Rectangle class
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Returns the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width value
        Args:
            value: the value to be set to width attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of th rectangle object"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height value
        Args:
            value: the height value to be set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area
        Takes width and height and multiplies"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the addition of each side of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
