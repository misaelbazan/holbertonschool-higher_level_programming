#!/usr/bin/python3
"""This module contains 01 class, and imports 01 class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Import BaseGeometry class from 7-base_geometry"""


class Rectangle(BaseGeometry):
    """This class inherits from BaseGeometry:
    Inherited methods:
        area(BaseGeometry): returns an exception
        integer_validation(self, name, value):
        Return:
            True if "value" argument is integer, False otherwise
    """
    def __init__(self, width, height):
        """Initializesa new instance from the class Rectangle:
        Args:
            width: width of the new rectangle
            height: height of the new rectangle
        """
        super().__init__()
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the class-name between [] following by <width>/<height>
        [Rectangle] 5/8 for example
        """
        return f"[{__class__.__name__}] {self.__width}/{self.__height}"
