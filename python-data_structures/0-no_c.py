#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char == 'c' or char == 'C':
            del char
        else:
            new_string = new_string + char
    return new_string
