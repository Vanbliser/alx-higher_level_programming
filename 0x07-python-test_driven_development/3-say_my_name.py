#!/usr/bin/python3

"""Contains the function say_my_name()"""


def say_my_name(first_name, last_name=""):
    """a function that prints My name is <first name> <last name>

    Args:
        first_name (string): The first name
        last_name (string, optional): the last name. Defaults to empty string
    Raises:
        TypeError: if first_name and last_name are not of type string
    """
    msg0 = "first_name must be a string"
    msg1 = "last_name must be a string"
    if not isinstance(first_name, str) or isEmptyOrWhitespace(first_name):
        raise TypeError(msg0)
    if not isinstance(last_name, str):
        raise TypeError(msg1)
    first_name = first_name.strip()
    last_name = last_name.strip()
    print(f"My name is {first_name} ", end="")
    if not isEmptyOrWhitespace(last_name):
        print(f"{last_name}", end="")
    print()


def isEmptyOrWhitespace(s):
    """check if a string is empty or whitespace

    Args:
        s (string): the string to check

    Returns:
        bool: True if s is empty or whitespace, else False
    """
    if s.isspace() or len(s) == 0:
        return True
    return False
