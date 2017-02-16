#!/usr/bin/env python

def prime_factores(number):
    """
    Generate a list of prime factores below number.
    """
    n = 2
    factores = []
    while n * n < number:
        while number % n == 0:
            number //= n
            factores.append(n)
        n += 1

    if number != 1:
        factores.append(number)

    return factores

if __name__ == '__main__':
    print(max(prime_factores(600851475143)))
