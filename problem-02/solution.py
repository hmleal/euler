#!/usr/bin/env python


def fibonacci():
    """
    Calculate sum of all fibonacci even-numbers below 4000000
    """
    a, b = 1, 2
    _sum = 0
    while a < 4000000:
        if a % 2 == 0:
            _sum += a
        a, b = b, a+b

    return _sum


if __name__ == '__main__':
    print(fibonacci())
