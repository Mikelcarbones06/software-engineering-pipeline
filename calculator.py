import math


def add(a, b):
    return a + b


def sub(a, b):
    return a - b
def multiply(a, b):
    return a * b

def power(a, b):
    return a ** b

def ln(value):
    if value <= 0:
        raise ValueError("ln is only defined for positive values")
    return math.log(value)


def log(value, base=10):
    if value <= 0:
        raise ValueError("log is only defined for positive values")
    if base <= 0 or base == 1:
        raise ValueError("log base must be positive and different from 1")
    return math.log(value, base)
def sqrt(a):
    return  a**(1/2)
