#!/usr/bun/python3
"""Contains def read_file(filename="") function"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): the filename to read. Default to empty string
    """
    with open(filename) as file:
        while (line := file.readline()):
            print(line, end="")
