#!/usr/bin/python3

def uppercase(str):
    # A function that prints a string in uppercase followed by a new line.

    for c in str:
        char_int = ord(c)
        if (char_int >= 97 and char_int <= 122):
            char_int -= 32
        print("{:c}".format(char_int), end="")
    print()
