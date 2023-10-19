#!/usr/bin/python3
"""This module contains: 01 classes"""


class BaseGeometry:
    """Base Geometry is in construction"""
    def area(self):
        """This method is raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates if value is int
        If not, it raises two errors, with their respective messages
        """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
