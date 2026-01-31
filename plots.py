import math
import matplotlib.pyplot as plt
import os

# Ensure image directory exists
IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)


def plot_greedy_runtime(results):
    plt.figure()

    for algo in ["EFT", "EST", "SD"]:
        xs = [n for name, n, _, _ in results if name == algo]
        ys = [t for name, _, t, _ in results if name == algo]
        plt.plot(xs, ys, marker="o", label=algo)

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("n")
    plt.ylabel("Runtime (s)")
    plt.title("Greedy Algorithms Runtime")
    plt.legend()

    plt.savefig(f"{IMAGE_DIR}/greedy_runtime.png", dpi=300, bbox_inches="tight")
    plt.close()


def plot_greedy_normalized(results):
    plt.figure()

    for algo in ["EFT", "EST", "SD"]:
        xs = []
        ys = []
        for name, n, t, _ in results:
            if name == algo:
                xs.append(n)
                ys.append(t / (n * math.log2(n)))

        plt.plot(xs, ys, marker="o", label=algo)

    plt.xlabel("n")
    plt.ylabel(r"$t(n) / (n \log n)$")
    plt.title("Normalized Greedy Runtime")
    plt.legend()

    plt.savefig(f"{IMAGE_DIR}/greedy_normalized.png", dpi=300, bbox_inches="tight")
    plt.close()


def plot_exhaustive(results):
    plt.figure()

    xs = [n for n, _, _ in results]
    ys = [t for _, t, _ in results]

    plt.plot(xs, ys, marker="o")
    plt.xlabel("n")
    plt.ylabel("Runtime (s)")
    plt.title("Exhaustive Algorithm Runtime")

    plt.savefig(f"{IMAGE_DIR}/exhaustive_runtime.png", dpi=300, bbox_inches="tight")
    plt.close()
