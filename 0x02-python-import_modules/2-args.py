#!/usr/bin/python3
i = 0
if __name__ == '__main__':
    import sys
    n = len(sys.argv)
    if len(sys.argv) - 1 == 0:
        print("{} arguments.".format((len(sys.argv)-1)))
    elif len(sys.argv) - 1 == 1:
        print("{} argument:".format((len(sys.argv)-1)))
    elif len(sys.argv) > 1:
        print("{} arguments:".format((len(sys.argv)-1)))
    for i in range(1, n):
        print("{}: {}".format(i, sys.argv[i]))
