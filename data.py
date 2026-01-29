# dataset 
import random

def generate_intervals(n, D, alpha, seed=None):
    """
    Generate n intervals with controlled overlap.

    Parameters:
        n     : number of intervals
        D     : max duration
        alpha : overlap control parameter
        seed  : random seed (optional)

    Returns:
        List of (start, finish) intervals
    """
    if seed is not None:
        random.seed(seed)

    T = alpha * n * D
    intervals = []

    for _ in range(n):
        s = random.uniform(0, T)
        d = random.uniform(1, D)
        f = s + d
        intervals.append((s, f))

    return intervals