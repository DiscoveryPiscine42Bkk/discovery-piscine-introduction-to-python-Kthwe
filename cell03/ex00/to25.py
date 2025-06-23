#!/usr/bin/env python3

num = int(input("Enter a number less than 25 : "))
if num < 25:
    for i in range(num,26,1):
        print(f"Inside the loop, my variable is {i}")
else:
    print("Error")
