#!/usr/bin/python3
"""Contains def write_file(filename="", text="") function"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename (str): the filename to write to
        text (str): the text to write

    Returns:
        int: the number of characters written
    """
    with open(filename, mode='w',  encoding='utf-8') as file:
        length = file.write(text)
    return length
