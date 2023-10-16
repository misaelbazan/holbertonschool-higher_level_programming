#!/usr/bin/python3
"""Class Rectangle:
    Define a rectangle
"""


class Rectangle:
    """This class defines a rectangle object
    """
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        """Initialize a new object from the Rectangle class
        Args:
            width (int): the rectangle's width
            height (int): the rectangle's height
        """
        Rectangle.number_of_instances += 1
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle
        Args:
            value (int): value to be set as width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle
        Args:
            value (int): value to be set as height
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
        """Returns the rectangle perimeter"""
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns a string that contains a rectangle of #'s"""
        if self.__width == 0 or self.__height == 0:
            return("")
        if isinstance(Rectangle.print_symbol, list):
            symbol_str = "\n".join(["".join(map(str, Rectangle.print_symbol)) \
                * self.__width for rows in range(self.__height)])

        else:
            symbol_str = "\n".join([str(Rectangle.print_symbol) * self.__width \
                    for rows in range(self.__height)])
        return symbol_str

    def __repr__(self):
        """Returns a Rectangle class string representation"""
        return f'{self.__class__.__name__}({self.__width}, {self.__height})'

    def __del__(self):
        """Prints a message each time a rectangle object is deleted
        Decreases by -1 the number of instances variable counter
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
