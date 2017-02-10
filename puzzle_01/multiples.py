#!/usr/bin/env python


def get_sum(limit):
    """
    Get sum of all multiples of 3 and 5 between 0 and limit.
    """
    return sum([x for x in range(limit) if x % 3 == 0 or x % 5 == 0])
