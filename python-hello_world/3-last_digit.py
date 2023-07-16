#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
s_num = "Last digit of "
if (last > 5):
    print(s_num +"{} is {} and is greater than 5".format(str(number), str(last)))
elif (last == 0):
    print(s_num +"{} is {} and is 0".format(str(number), str(last)))
elif (last < 6 and last != 0):
    print(s_num +"{} is {} and is less than 6 and not 0".format(str(number), str(last)))
