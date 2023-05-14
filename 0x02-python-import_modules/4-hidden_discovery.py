#!/usr/bin/python3
import hidden_4 as h
if __name__ == '__main__':
    for i in dir(h):
        if i[1] == '_':
            continue
        else:
            print(i)
