#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ != "__main__":
    exit()

args = len(argv) - 1
if args != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
if argv[2] == '+':
    operator = add
elif argv[2] == '-':
    operator = sub
elif argv[2] == '*':
    operator = mul
elif argv[2] == '/':
    operator = div
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

a = int(argv[1])
b = int(argv[3])
total = operator(a, b)
print(a, argv[2], b, "=", total)
