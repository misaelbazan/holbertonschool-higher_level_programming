#!/usr/bin/python3
"""Class Rectangle:
    Define a rectangle
"""


class Rectangle:
    """This class defines a rectangle object"""
    def __init__(self, width=0, height=0):
        """Initialize a new object from the Rectangle class
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
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
            value: the width value to be set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height value"""
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
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """Returns and string of #'s that draws the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for rows in range(self.__height):
            for columns in range(self.__width):
                rectangle_str += "#"
            if rows < self.__height - 1:
                rectangle_str += "\n"

        return(rectangle_str)
