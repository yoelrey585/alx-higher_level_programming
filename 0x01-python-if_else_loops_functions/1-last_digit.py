#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastDigit = number % -10
else:
    lastDigit = number % 10
if lastDigit > 5:
    print(f"Last digit of {number} is {lastDigit} and is greater than 5")
elif lastDigit < 6 and lastDigit != 0:
       print("Last digit of {:d} is {:d} and is less than 6 and not 0"
        .format(number, lastDigit))
else:
    print(f"Last digit of {number} is 0 and is 0")
