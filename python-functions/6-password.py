#!/usr/bin/python3
def validate_password(password):
    '''validates a password'''
    if len(password) < 8:
        return False
    if " " in password:
        return False
    for upper in password:
        if upper.isupper():
            for lower in password:
                if lower.islower():
                    for numeric in password:
                        if numeric.isnumeric():
                            return True
    return False
