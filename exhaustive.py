# exponential optimal solver

from itertools import combinations

def is_compatible_set(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


def exhaustive_optimal(intervals):
    """
    Returns the maximum-size compatible subset.
    Exponential time: O(n 2^n)
    """
    n = len(intervals)
    best = []

    for r in range(1, n + 1):
        for subset in combinations(intervals, r):
            if is_compatible_set(subset):
                if len(subset) > len(best):
                    best = subset

    return best
