# 3 greedy algorithms

def greedy_schedule(intervals, key):
    intervals = sorted(intervals, key=key)

    selected = []
    last_finish = float('-inf')

    for s, f in intervals:
        if s >= last_finish:
            selected.append((s, f))
            last_finish = f

    return selected


def greedy_EFT(intervals):
    """Earliest Finish Time"""
    return greedy_schedule(intervals, key=lambda x: x[1])


def greedy_EST(intervals):
    """Earliest Start Time"""
    return greedy_schedule(intervals, key=lambda x: x[0])


def greedy_SD(intervals):
    """Shortest Duration"""
    return greedy_schedule(intervals, key=lambda x: x[1] - x[0])
