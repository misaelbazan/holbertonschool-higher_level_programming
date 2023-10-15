#!/usr/bin/python3
"""Class Rectangle:
    Define a rectangle
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return("")
        rectangle_str = ""
        for rows in range(self.__height):
            for columns in range(self.__width):
                rectangle_str += "#"
            if rows < self.__height - 1:
                rectangle_str += "\n"

        return(rectangle_str)
