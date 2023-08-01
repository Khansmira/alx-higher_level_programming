#!/usr/bin/python3
"""
a class that defines a Square
private instance attribute: size
"""


square1 = __import__("1-square").Square


class Square(square1):
    """ a class that defines a Square
    Args:
        square1 (class): a class which defines a Square with private attribute size
    """

    def __init__(self, size=0):
        """initializing square

        Args:
            size (int): the size of the square passed. dafault value 0

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        square1.__size = size
        self.__size = square1.__size

        if type(square1.__size) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif square1.__size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size
