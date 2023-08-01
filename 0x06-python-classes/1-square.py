#!/usr/bin/python3
"""
This class defines a square
private instance attribute: size
 """

square0 = __import__("0-square").Square


class Square(square0):
    """ an inherited class from Square definition class
    Args:
        square0 (class): a class which defines a square
    """

    def __init__(self, size):
        """initialization function
        Args:
            size: an instance attribute
        """
        self.__size = size
