#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    i = str[:n] + str[n + 1:]
    return "{:s}".format(i)
