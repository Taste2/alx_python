#!/usr/bin/python3
def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    number_root = number ** 0.5
    for i in range(2, int(number_root+1)):
        if number % i == 0:
            return False
    return True
