#!/usr/bin/env python3

num = input("Give me a number: ")
number = float(num)
if number.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")