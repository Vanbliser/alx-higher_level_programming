#!/usr/bin/python3
import sys
if __name__ == '__main__':
    len_of_arg = len(sys.argv) - 1
    if len_of_arg == 0:
        print("{} arguments.".format(len_of_arg))
    else:
        if len_of_arg == 1:
            print("{} argument:".format(len_of_arg))
        else:
            print("{} arguments:".format(len_of_arg))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
