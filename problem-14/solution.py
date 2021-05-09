#!/usr/bin/env python

CACHE = {}


def collatz(limit):

    if limit == 1:
        return (1, 1)

    original_number = limit
    chain = 1

    while limit != 1:
        if limit % 2 == 0:
            limit //= 2
        else:
            limit = limit * 3 + 1

        chain += 1

        if limit in CACHE.keys():
            CACHE[original_number] = chain + CACHE[limit]
            return (original_number, CACHE[original_number])

    CACHE[original_number] = chain

    return (original_number, CACHE[original_number])


if __name__ == "__main__":
    chain = 0
    biggest_number = 0
    for x in range(1, 1000000):
        number, seq = collatz(x)
        if seq > chain:
            chain = seq
            biggest_number = number

    print(biggest_number)
