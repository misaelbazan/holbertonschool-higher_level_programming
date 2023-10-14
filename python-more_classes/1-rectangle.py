#!/usr/bin/python3
"""Class Rectangle:
    Define a rectangle
"""
class Rectangle:
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        def height(self, value):
            if not isinstance(height, int):
                raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError("height must be >= 0")
            return self.__height
        def width(self, value):
            if not isinstange(width, int):
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")
            return self.__width
