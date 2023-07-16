#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
s_num = "Last digit of"
if (last_digit > 5):
    print(s_num + "{} is {} and is greater than 5".format(str(number), str(last_digit)))
elif (last_digit == 0):
    print(s_num + "{} is {} and is 0".format(str(number), str(last_digit)))
elif (last_digit < 6 and last_digit != 0):
    print(s_num + "{} is {} and is less than 6 and not 0")
