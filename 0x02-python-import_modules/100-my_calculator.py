#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':

    argv = sys.argv
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if argv != 4:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif
    print("{} {} {} = {}".format(a, operator, b, r))
            
