#!/usr/bin/env python


def sum_of_squares(n):
    # TODO refactore
    return sum([x ** 2 for x in range(1, n + 1)])


def square_sum(n):
    return (n * (n + 1) / 2) ** 2


if __name__ == "__main__":
    print(square_sum(100) - sum_of_squares(100))
