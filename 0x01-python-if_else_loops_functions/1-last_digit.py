#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = abs(number) % 10
if number < 0:
    ldigit = -ldigit
print("Last digit of {} is {} and is ".format(number, ldigit), end="")
if ldigit > 5:
    print("greater than 5")
elif ldigit == 0:
    print("0")
else:
    print("less than 6 and not 0")
