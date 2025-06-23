#!/usr/bin/env python3
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
res = int(num1)*int(num2)
print(f"{num1} x {num2} = {res}")
if int(res) < 0:
    print("This result is negative.")
elif int(res) > 0:
    print("This result is positive.")
else:
    print("This result is both positive and negative.")
