#!/usr/bin/python3
def print_last_digit(number):
    ln = number % 10
    ln1 = (number * -1) % 10
    if number >= 0:
        print("{}".format(ln), end="")
        return ln
    else:
        print("{}".format(ln1), end="")
        return ln1
