#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of "

if number > 0:
    lastDigit = number % 10
else:
    lastDigit = number % -10

if lastDigit > 5:
    print("{}{} is {} and is greater than 5".format(str1, number, lastDigit))
elif lastDigit == 0:
    print("{}{} is {} and is 0".format(str1, number, lastDigit))
elif lastDigit < 6:
    print("{}{} is {} and is less than 6 and not 0".format(str1, number, lastDigit))
