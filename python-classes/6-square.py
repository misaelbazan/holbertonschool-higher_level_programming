#!/usr/bin/python3
"""This module contains 1 classes
"""


class Square:
    """This class represents a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square

        Args:
            size (int): the size of the new square
            position (int): the position in coordinates of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size's value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the square's actual position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position's value"""
        if type(value) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) and type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] and value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """Returns the square area"""
        return self.__size**2

    def my_print(self):
        """prints to stdout square with the char #"""
        if self.size == 0:
            print()
        else:
            a, b = self.position
            for line in range(b):
                print()
            for line in range(self.size):
                print(' ' * a, end='')
                print('#' * self.size)
