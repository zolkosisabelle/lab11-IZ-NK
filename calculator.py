# Partner 1: Isabelle Zolkos
# Partner 2: Nikhil Karri
import math

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def sub(a, b):
    return subtract(a, b)


def multiply(a, b):
    return a * b


def mul(a, b):
    return multiply(a, b)


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("The divisor cannot be zero.")
    return b / a


def div(a, b):
    return divide(a, b)


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm arguments.")
    return math.log(b, a)


def log(a, b):
    return logarithm(a, b)


def exponent(a, b):
    return a ** b


def exp(a, b):
    return exponent(a, b)


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)
