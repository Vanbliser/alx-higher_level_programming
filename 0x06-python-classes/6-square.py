#!/usr/bin/python3

"""Contains a class Square.

"""


class Square:
    """A class square."""

    def __init__(self, size=0, position=(0, 0)):
        """constructor to initialize a class."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """property getter size

        size must be an integer. If size is less than 0, raise an exception
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not (isinstance(value, int)):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """position of a square.

        position must be a tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple)
                and len(value) == 2
                and isinstance(value[0], int)
                and isinstance(value[1], int)):
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """area of a suare.

        Returns:
            the area of square
        """
        return (self.size)**2

    def my_print(self):
        """prints in stdout the square with the character #"""

        if self.size == 0:
            print()
        else:
            if self.position[1] > 0:
                for y in range(abs(self.position[1])):
                    print()
            for col in range(self.size):
                print(' '*(self.position[0]), '#'*(self.__size), sep="")
            if self.position[1] < 0:
                for y in range(abs(self.position[1])):
                    print()
