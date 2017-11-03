#!/usr/bin/env python

if __name__ == '__main__':
    maxp = 0

    for x in range(100, 1000):
        for j in range(x, 1000):
            number = x * j
            if str(number) == str(number)[::-1] and number > maxp:
                maxp = number

    print(maxp)
