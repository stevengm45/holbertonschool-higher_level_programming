#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    suma = 0
    nums = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    for i, next in zip(roman_string, roman_string[1:]):
        if nums[i] >= nums[next]:
            suma += nums[i]
        else:
            suma -= nums[i]
    suma += nums[roman_string[-1]]
    return suma
