#!/usr/bin/env python3

print("Enter a number less than 25")
num = int(input())
if num < 25:
    print(num)
    for i in range(num,26,1):
        print(f"Inside the loop, my variable is {i}")
else:
    print("Error")