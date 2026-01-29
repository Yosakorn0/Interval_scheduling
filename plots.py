import math
import matplotlib.pyplot as plt


def plot_greedy_runtime(results):
    for algo in ["EFT", "EST", "SD"]:
        xs = [n for name, n, _, _ in results if name == algo]
        ys = [t for name, _, t, _ in results if name == algo]
        plt.plot(xs, ys, label=algo)

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("n")
    plt.ylabel("Runtime (s)")
    plt.title("Greedy Algorithms Runtime")
    plt.legend()
    plt.show()


def plot_greedy_normalized(results):
    for algo in ["EFT", "EST", "SD"]:
        xs = []
        ys = []
        for name, n, t, _ in results:
            if name == algo:
                xs.append(n)
                ys.append(t / (n * math.log2(n)))

        plt.plot(xs, ys, label=algo)

    plt.xlabel("n")
    plt.ylabel("t(n) / (n log n)")
    plt.title("Normalized Greedy Runtime")
    plt.legend()
    plt.show()


def plot_exhaustive(results):
    xs = [n for n, _, _ in results]
    ys = [t for _, t, _ in results]

    plt.plot(xs, ys, marker="o")
    plt.xlabel("n")
    plt.ylabel("Runtime (s)")
    plt.title("Exhaustive Algorithm Runtime")
    plt.show()
