def add(x, y):
    """Add function"""
    return x + y


def substract(x, y):
    """Substract function"""
    return x + y

def multiply(x, y):
    """Multiply function"""
    return x * y

def divide(x, y):
    """Divide function"""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x/y

def square(x):
    """Return square root of the given argument"""

    if x < 0:
        raise ValueError("Cannot square the negative number")
    return x**0.5