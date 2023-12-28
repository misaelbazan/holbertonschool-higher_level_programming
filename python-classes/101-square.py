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
        if not isinstance(value, tuple) or len(value) != 2 or\
                not all(isinstance(num, int) for num in value) or\
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
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

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                if i != self.__size - 1:
                    print("")
        return ("")
