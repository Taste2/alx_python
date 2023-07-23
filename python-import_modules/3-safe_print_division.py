#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, UnboundLocalError):
        return 0
    finally:
        print("{} / {} = {}".format(a, b, result))
