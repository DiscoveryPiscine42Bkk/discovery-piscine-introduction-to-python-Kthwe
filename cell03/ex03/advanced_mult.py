#!/usr/bin/env python3
for i in range(0, 11, 1):
    print(f"Table de {i}: ", end="")
    for j in range(0, 11, 1):
        print(f"{i*j} ", end="")
    print()