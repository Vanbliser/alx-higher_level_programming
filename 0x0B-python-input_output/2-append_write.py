#!/usr/bin/python3
"""contains def append_write(filename="", text="") function"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added.

    Args:
        filename (str): the name of the file
        text (str): the text to append

    Returns:
        int: the number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        length = file.write(text)
    return length
