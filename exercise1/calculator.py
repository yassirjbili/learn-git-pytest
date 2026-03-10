def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def add(a: Number, b: Number) -> Number:
    return a+b




def subtract(a: Number, b: Number) -> Number:
    return a - b
    


def multiply(a: Number, b: Number) -> Number:
    return a * b


def divide(a: Number, b: Number) -> Number:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
