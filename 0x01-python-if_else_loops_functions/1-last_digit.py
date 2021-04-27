#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of"
ln = number % 10
ln1 = ((number * -1) % 10)*(-1)

if ln > 5:
    print(str1, number, "is", ln, "and is greater than 5")
elif ln == 0:
    print(str1, number, "is", ln, "and is 0")
else:
    print(str1, number, "is", ln1, "and is less than 6 and not 0")
