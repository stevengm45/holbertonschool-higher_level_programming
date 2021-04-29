#!/usr/bin/python3
i = 0
if __name__ == '__main__':
    import sys
    n = len(sys.argv)
    if len(sys.argv) - 1 == 0:
        print((len(sys.argv)-1), "arguments.")
    elif len(sys.argv) - 1 == 1:
        print((len(sys.argv)-1), "argument:")
    elif len(sys.argv) > 1:
        print((len(sys.argv)-1), "arguments:")
    for i in range(1, n):
        print(i, ":", sys.argv[i])
