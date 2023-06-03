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
                and isinstance(value[1], int)
                and (value[0] >= 0)
                and (value[1] >= 0)):
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
            for y in range(self.position[1]):
                print()
            for col in range(self.size):
                print(' '*(self.position[0]), '#'*(self.__size), sep="")

    def __str__(self):
        """printable output for Square"""
        string = ""
        if self.size == 0:
            return string
        else:
            for y in range(self.position[1]):
                string += "\n"
            for col in range(self.size):
                i = ' '*(self.position[0])
                j = '#'*(self.__size)
                if col < ((self.size) - 1):
                    string += f"{i}{j}\n"
                else:
                    string += f"{i}{j}"
            return string
