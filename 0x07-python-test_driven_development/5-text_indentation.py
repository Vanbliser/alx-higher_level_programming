#!/usr/bin/python3

"""Contains text_indentation(text) function"""


def text_indentation(text=None):
    """a function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text (string): the string to format
    """
    if text is None:
        raise TypeError("text must be a string")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = text.replace('?', '?\n\n? ').replace(':', ':\n\n? ').replace(
            '.', '.\n\n? ')
    splited_text = new_text.split('? ')
    for index, line in enumerate(splited_text):
        if len(line) == 0:
            break
        print(line.lstrip(), end="")
