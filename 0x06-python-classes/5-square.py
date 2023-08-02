#!/usr/bin/python3
""" a class that defines  square with private instance """


class Square():
    """ calculates area of the square and defines private instance size """

    def __init__(self, size=0):
        """initializing size

            Args:
            size (int): the size of the square passed. Defaults to 0.

        exceptions:
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
            value: a new size value of type int

        exceptions:
            TypeError: if not integer
            ValueError: if < 0
        """

        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """ finds area of the square

        Returns:
            int: the are of the square
        """
        return (self.__size**2)

    def my_print(self):
        """printing the square"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()
