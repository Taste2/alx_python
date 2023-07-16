#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
s_num = "Last digit of "
greater = " and is greater than "
negative = " and is less than 6 and not "
if (last > 5):
    print(s_num + "{0} is {1}" + greater + "5".format(str(number), str(last)))
elif (last == 0):
    print(s_num + "{} is {} and is 0".format(str(number), str(last)))
elif (last < 6 and last != 0):
    print(s_num + "{0} is -{1}" + negative + "0".format(str(number), str(last)))
