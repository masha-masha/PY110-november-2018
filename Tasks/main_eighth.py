"""
Useless module
"""

import os

import numpy as np

CONST = 3.14

def func1(a: int, b: str) -> np.ndarray:
    """
    func1

    useless function1
    :param a: la
    :param b: lala
    :return: lalala
    """
    return np.array([1])

def func2(a: int, b: str) -> np.ndarray:
    """
    func2

    useless function2
    :param a: la
    :param b: lala
    :return: lalala
    """
    return np.array([1, 1])

def func3(a: int, b: str) -> np.ndarray:
    """
    func3

    useless function3
    :param a: la
    :param b: lala
    :return: lalala
    """
    return np.array([1, 1, 1])


if __name__ == "__main__":
    print(func1(1, ''))
    print(func2(1, ''))
    print(func3(1, ''))
