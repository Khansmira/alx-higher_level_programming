#!/usr/bin/python3
"""
a class that defines a square
private instance: size
public method : area
"""


class Square():
    """ a class to defines and calculates area of the square """

    def __init__(self, size=0):
        """initializing size

        Args:
            size (int): the size of the square passed. Defaults to 0.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        self.__size = size
        if type(self.__size) != int:
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """ finding the area of the square

        Returns:
            int: the are of the square
        """
        return (self.__size**2)
