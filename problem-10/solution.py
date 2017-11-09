#!/usr/bin/env python


def primes(limit):
    """
    Return a generator for prime numbers.

    Args:
      limit (int): The maximun prime number

    This algorith uses the Sieve of Eratosthenes
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    a = [True] * limit

    a[0] = False
    a[1] = False

    for i, is_prime in enumerate(a):
        if is_prime:
            yield i

            for n in range(i*i, limit, i):
                a[n] = False


if __name__ == '__main__':
    print(sum([p for p in primes(2000000)]))
