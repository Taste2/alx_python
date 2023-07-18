#!/usr/bin/python3
def fibonacci_sequence(n):
    '''Returns the fibonacci sequence
    of a given number'''
    if n == 2:
        list_ = [0, 1]
        return list_
    elif n == 1:
        list_ = [0]
        return list_
    elif n <= 0:
        list_ = []
        return list_
    elif n > 2:
        n = n - 2
        list_ = [0, 1]
        for i in range(n):
            list_.append(list_[-1] + list_[-2])
        return list_
