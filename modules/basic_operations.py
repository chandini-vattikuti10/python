'''1. Create a module named basic_operations that includes functions for addition, subtraction, 
multiplication, and division. Each function should take two arguments and return the result of the respective operation.'''


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
