# benchmark.py
import time
import numpy as np

from data import generate_intervals
from greedy import greedy_EFT, greedy_EST, greedy_SD
from exhaustive import exhaustive_optimal
from plots import (
    plot_greedy_runtime,
    plot_greedy_normalized,
    plot_exhaustive,
    plot_exhaustive_normalized
)

def time_algorithm(func, intervals, trials=10):
    times = []

    # warm-up
    func(intervals)

    for _ in range(trials):
        start = time.perf_counter()
        func(intervals)
        end = time.perf_counter()
        times.append(end - start)

    return np.mean(times), np.std(times)


def benchmark_greedy(n_values, D, alpha, trials=10):
    results = []

    for n in n_values:
        intervals = generate_intervals(n, D, alpha)

        for name, algo in [
            ("EFT", greedy_EFT),
            ("EST", greedy_EST),
            ("SD", greedy_SD),
        ]:
            mean, std = time_algorithm(algo, intervals, trials)
            results.append((name, n, mean, std))

    return results


def benchmark_exhaustive(n_values, D, alpha, trials=3):
    results = []

    for n in n_values:
        intervals = generate_intervals(n, D, alpha)
        mean, std = time_algorithm(exhaustive_optimal, intervals, trials)
        results.append((n, mean, std))

    return results


if __name__ == "__main__":
    # ===============================
    # PARAMETERS
    # ===============================
    D = 10
    alpha = 1 # change to 1 and 5 for other regimes

    # ===============================
    # GREEDY EXPERIMENTS (REQUIRED)
    # n = 2^10 ... 2^20
    # ===============================
    n_values_greedy = [2**k for k in range(10, 21)]
    trials_greedy = 10

    print("Benchmarking Greedy Algorithms")
    print("=" * 60)

    greedy_results = benchmark_greedy(
        n_values_greedy, D, alpha, trials_greedy
    )

    for name, n, mean, std in greedy_results:
        print(f"{name} (n={n}): {mean:.6f} ± {std:.6f} seconds")

    # PLOTS FOR GREEDY
    plot_greedy_runtime(greedy_results)
    plot_greedy_normalized(greedy_results)

    # ===============================
    # EXHAUSTIVE EXPERIMENTS
    # n = small only
    # ===============================
    n_values_exhaustive = [5, 10, 15, 20]
    trials_exhaustive = 3

    print("\nBenchmarking Exhaustive Algorithm")
    print("=" * 60)

    exhaustive_results = benchmark_exhaustive(
        n_values_exhaustive, D, alpha, trials_exhaustive
    )

    for n, mean, std in exhaustive_results:
        print(f"Exhaustive (n={n}): {mean:.6f} ± {std:.6f} seconds")

    # PLOT FOR EXHAUSTIVE
    plot_exhaustive(exhaustive_results)
    plot_exhaustive_normalized(exhaustive_results)