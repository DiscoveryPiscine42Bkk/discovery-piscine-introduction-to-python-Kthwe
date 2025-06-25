#!/usr/bin/env python3

def average(scores):
    if not scores:
        return 0  # Avoid division by zero
    return sum(scores.values()) / len(scores)

# Example dictionaries
class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}
class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

# Output
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
