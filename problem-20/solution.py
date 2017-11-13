#!/usr/bin/env python
import math


def factorial_recursive(number):
    """Return number factorial.

    The recursive method
    """
    if number == 0:
        return 1
    return number * factorial_recursive(number-1)


def factorial(number):
    """Return number factorial.

    The simple implementation
    """
    prod = 1
    for n in range(1, number+1):
        prod = prod * n

    return prod


if __name__ == '__main__':
    print(sum([int(number) for number in str(math.factorial(100))]))
