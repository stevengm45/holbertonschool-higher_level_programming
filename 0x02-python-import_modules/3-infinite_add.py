#!/usr/bin/python3
import sys
if __name__ == '__main__':
    print("{}".format(sum(int(i) for i in sys.argv[1:])))
