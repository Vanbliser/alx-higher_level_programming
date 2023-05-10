#!/usr/bin/python3

def remove_char_at(str1, n):
    str_cpy = ""
    for i in range(len(str1)):
        if (i == n):
            continue
        str_cpy = "{0}{1}".format(str_cpy, str1[i])
    return str_cpy
