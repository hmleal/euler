#!/usr/bin/env python


def grid_traveler(m, n, memo=None):
    if memo is None:
        memo = {}

    key = f"{m},{n}"

    if memo.get(key):
        return memo[key]

    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    memo[key] = grid_traveler(m - 1, n, memo) + grid_traveler(m, n - 1, memo)

    return memo[key]


if __name__ == "__main__":
    print(f"Result: {grid_traveler(21, 21)}")
