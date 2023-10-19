#!/usr/bin/python3
"""This module contains 01 class, and imports 01 class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Import BaseGeometry class from 7-base_geometry"""


class Rectangle(BaseGeometry):
    """This class inherits from BaseGeometry:
    Inherited methods:
        area(BaseGeometry): returns an exception
        integer_validation(BaseGeometry): takes two parameters
    """
    def __init__(self, width, height):
        super().__init__()
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
