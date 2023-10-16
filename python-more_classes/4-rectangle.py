#!/usr/bin/python3
"""Class Rectangle:
    Define a rectangle
"""


class Rectangle:
    """
    This class defines a rectangle

    Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """Initialize a new object from Rectangle class
        Args:
            height (int): the height of the rectangle
            width (int): the width of the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width value fro the outside
        Args:
            value (int): value passed to be set as the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height value from the outside

        Args:
            value (int): value passed to be set as the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns a string representation of the rectangle of #'s"""
        if self.__width == 0 or self.__height == 0:
            return("")
        rectangle_str = ""
        for rows in range(self.__height):
            for columns in range(self.__width):
                rectangle_str += "#"
            if rows < self.__height - 1:
                rectangle_str += "\n"

        return(rectangle_str)

    def __repr__(self):
        """Returns a string representation of the rectangle to recreate \
        a new instance using eval()"""
        return f'{self.__class__.__name__}({self.__width}, {self.__height})'
