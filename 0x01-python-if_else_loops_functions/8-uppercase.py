#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord("a") and ord(i) <= ord("z"):
            i = chr(ord(i) - ord(" "))
        print("{:s}".format(i), end="")
    print("\n", end="")
