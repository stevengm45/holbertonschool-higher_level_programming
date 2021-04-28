#!/usr/bin/python3
i = 96
while i < 122:
      i += 1
      if i == 101:
            continue
      if i == 113:
            continue
      print("{}".format(chr(i)), end="")
