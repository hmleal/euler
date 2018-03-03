#!/usr/bin/env python


def fib():
    a, b = 1, 1

    while True:
        a, b = a + b
        yield a


if __name__ == '__main__':
    a, b, i = 1, 1, 1

    limit = 1000

    while len(str(a)) < limit:
        a, b, i = b, a + b, i + 1

    print(i, a)