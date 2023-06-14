#!/usr/bin/python3

"""Contains print_square(size) function"""


def print_square(size):
    """a function that prints a square with the character #.

    Args:
        size (int): size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size == size+1:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print(f"{size*'#'}")
