#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
big = "and is greater than 5"
small = "and is less than 6 and not 0"
draw = "and is 0"

if number > 0:
    end = number % 10
else:
    end = ((number * -1) % 10) * -1

if end > 5:
    final = big
elif end == 0:  # Use `==` for comparison
    final = draw
elif end < 6 and end != 0:  # Correctly check for non-zero values
    final = small

print("last digit of", number, "is", end, final)

