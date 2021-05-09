import math


def triangule():
    current = 1
    previous = 0

    while True:
        yield current + previous

        previous = current + previous
        current += 1


def divisors(n):
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.extend([i, n // i])
    divs.extend([n])

    return list(set(divs))


if __name__ == "__main__":
    for n in triangule():
        divs = divisors(n)

        if len(divs) > 500:
            break

    print(n)
