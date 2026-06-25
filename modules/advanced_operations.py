'''2. Develop another module named advanced_operations that contains functions for calculating the square root, 
exponentiation, and modulo of a given number. Ensure these functions handle potential errors, such as negative numbers for square root or 
division by zero.'''

import math


def square_root(num):
    if num < 0:
        return "Error: Cannot find square root of a negative number."
    return math.sqrt(num)


def exponentiation(base, power):
    return base ** power


def modulo(a, b):
    if b == 0:
        return "Error: Modulo by zero is not allowed."
    return a % b
