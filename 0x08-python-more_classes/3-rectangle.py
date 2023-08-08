#!/usr/bin/python3
"""
Defines a Rectangle
"""


class Rectangle:
    """
    A Rectangle
    """
    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        Getter for width of Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width of Rectangle
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height of Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for Height of Rectangle
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns area of Rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Returns perimeter of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = ""
        for i in range(self.__height):
            for x in range(self.__width):
                rect += "#"
            if i != self.__height - 1:
                rect = rect + "\n"
        return rect
