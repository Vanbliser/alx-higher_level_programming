#!/usr/bin/python3

def uppercase(str):
    # A function that prints a string in uppercase followed by a new line.
    
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - (ord('a') - ord('A')))
        print("{:s}".format(c), end='')
    print("")
