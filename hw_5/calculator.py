def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = 'b must not be zero!'
    return result
