#!/usr/bin/python3
""" a class that defines a square

private instance: size
public method: area

property: size getter
"""


class Square():
    """
    Args:
        square1 (class): a class that defines a square with size and area
    """

    def __init__(self, size=0):
        """initializing size

        Args:
            size (int): the size of the square passed. Default value  0

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        """getter for size

        Returns:
            integer: sends the value of private size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size

        Args:
            value (int): a new size value

        Raises:
            TypeError: if not integer
            ValueError: if < 0
        """

        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """ finding the area of the square

        Returns:
            int: the are of the square
        """
        return (self.__size**2)
