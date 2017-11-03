#!/usr/bin/env python


def collatz(limit):
    chain = [limit]
    while limit != 1:
        if limit % 2 == 0:
            limit //= 2
        else:
            limit = limit * 3 + 1
        chain.append(limit)
    return chain


if __name__ == '__main__':
    chain = []
    for x in range(1, 1000000):
        actual = collatz(x)
        if len(actual) > len(chain):
            chain = actual

    print(chain[0])
