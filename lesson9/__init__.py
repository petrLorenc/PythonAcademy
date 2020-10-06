import random


def buggy_function():
    error = random.choice([TypeError, ValueError, RuntimeError, ArithmeticError, FileNotFoundError, FloatingPointError])
    raise error()