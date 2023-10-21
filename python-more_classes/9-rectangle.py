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
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns a string that contains a rectangle of #'s"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            a = self.__height + 1
            b = self.__width
            str_repr = ''.join(
                    [f"{str(self.print_symbol) * b}\n" for i in range(a) if i])
            return str_repr[:len(str_repr) - 1]

    def __repr__(self):
        """Returns a Rectangle class string representation"""
        return f'{__class__.__name__}({self.__width}, {self.__height})'

    def __del__(self):
        """Prints a message each time a rectangle object is deleted
        Decreases by -1 the number of instances variable counter
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This is a static method
        Return:
            The biggest rectangle based on the area
            or rect_1 if boths have the same area
        """
        if isinstance(rect_1, Rectangle):
            area_1 = rect_1.area()
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle):
            area_2 = rect_2.area()
        else:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if area_1 > area_2 or area_1 == area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """This in a class method 
        Return:
            a new Rectangle instance with width == height == size
        """
        return Rectangle(size, size)
