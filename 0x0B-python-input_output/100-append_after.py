#!/usr/bin/python3
'''contain def append_after(filename="", search_string="", new_string="")'''


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file, after each line
    containing a specific string. You must use the with statement.
    You don’t need to manage file permission or file doesn't exist exceptions.

    Args:
        filename (str): name of file
        search_string (str): the string to search for
        new_string (str): the new string to insert
    """
    text = ''
    with open(filename, mode='r+') as file:
        while (line := file.readline()):
            text += line
            if line.find(search_string) >= 0:
                text += f"{new_string}"
    with open(filename, mode='w') as file:
        file.write(text)
