"""
Module Calc.py with 4 basic mathematics operations: +, -, / and *
"""


def add(a: int, b: int) -> int:
    """
    Function which return the sum of 2 integer numbers

    :param a: First number
    :param b: Second number
    :return: Sum of First and Second numbers
    """
    if not isinstance(a, int) and not isinstance(b, int):
        raise TypeError
    return a + b


def sub(a: int, b: int) -> int:
    """
    Function which return the subtraction of integer 2 numbers

    :param a: First number
    :param b: Second number
    :return: Subtraction of First and Second numbers
    """
    if not isinstance(a, int) and not isinstance(b, int):
        raise TypeError
    return a - b


def div(a: int, b: int) -> float:
    """
    Function which return the floor division product of integer 2 numbers

    :param a: First number
    :param b: Second number
    :return: Floor division product of First and Second numbers
    """
    if not isinstance(a, int) and not isinstance(b, int):
        raise TypeError
    if b == 0:
        raise ZeroDivisionError
    return a // b


def mul(a: int, b: int) -> int:
    """
    Function which return the multiply product of integer 2 numbers

    :param a: First number
    :param b: Second number
    :return: Multiply product of First and Second numbers
    """
    if not isinstance(a, int) and not isinstance(b, int):
        raise TypeError
    return a * b


if __name__ == "__main__":
    print("DON'T RUN ME!")
