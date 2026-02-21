#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        return None
    finally:
        print("Inside finally: {}".format(result))
    return result
