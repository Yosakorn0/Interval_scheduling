# Interval Scheduling: Empirical Runtime & Optimality Study

## Overview

This project implements and evaluates multiple algorithms for the
Interval Scheduling problem. The goal is to select the maximum number of
non-overlapping intervals from a given set.

The project includes: - Three greedy algorithms with different selection
criteria - An exhaustive exponential-time algorithm for optimal
solutions on small inputs - Synthetic dataset generation with controlled
overlap - Empirical runtime analysis and Big-O validation - Solution
quality comparison between greedy and optimal algorithms

------------------------------------------------------------------------

## Problem Definition

Given a set of intervals: I = {(s_i, f_i)} where s_i \< f_i

Two intervals are compatible if they do not overlap: f_i ≤ s_j or f_j ≤
s_i

**Objective:** Select a maximum-size subset of pairwise compatible
intervals.

------------------------------------------------------------------------

## Project Structure

    interval_scheduling/
    ├── benchmark.py     # Timing and experimental protocol
    ├── data.py          # Dataset generator with controlled overlap
    ├── exhaustive.py    # Exponential-time optimal solver
    ├── greedy.py        # Greedy interval scheduling algorithms
    ├── plots.py         # Runtime and Big-O validation plots
    └── README.md

------------------------------------------------------------------------

## Algorithms Implemented

### Greedy Algorithms (O(n log n))

Each greedy algorithm sorts the intervals using a specific criterion and
then scans to select compatible intervals.

-   **EFT**: Earliest Finish Time
-   **EST**: Earliest Start Time
-   **SD**: Shortest Duration

### Exhaustive Algorithm (O(n·2ⁿ))

-   Enumerates all subsets of intervals
-   Checks compatibility
-   Returns the largest feasible subset
-   Used only for small values of n

------------------------------------------------------------------------

## Dataset Generation

To ensure consistent overlap behavior as n increases, the time horizon
is defined as:

T = α · n · D

Where: - n is the number of intervals - D is the maximum interval
duration - α controls the overlap density

### Overlap Regimes

-   α = 0.1 → High overlap
-   α = 1 → Medium overlap
-   α = 5 → Low overlap

Intervals are generated using uniform distributions for start time and
duration.

------------------------------------------------------------------------

## How to Run Experiments

### Greedy Algorithms

Test for: n ∈ {2¹⁰, 2¹¹, ..., 2²⁰}

For each overlap regime (α = 0.1, 1, 5), run at least 10 trials and
record the mean and standard deviation.

### Exhaustive Algorithm

Test for small input sizes: n ∈ {5, 10, 15, ..., n_max}

n_max is chosen such that the algorithm completes in reasonable time.

All experiments are executed from **benchmark.py** and **plots.py**. No
command-line arguments are required.

### Step 1: Run Greedy Algorithm Experiments

Edit `benchmark.py` and ensure the following parameters are set:

``` python
n_values = [2**k for k in range(10, 21)]
D = 10
alpha = 0.1   # change to 1 and 5 for other regimes
trials = 10
```

Run:

``` bash
python benchmark.py
```

This will: - Generate datasets (excluding generation time from
measurements) - Run EFT, EST, and SD greedy algorithms - Record mean and
standard deviation of runtime

Repeat this step for: - α = 0.1 (high overlap) - α = 1 (medium
overlap) - α = 5 (low overlap)

Save the results for plotting.

------------------------------------------------------------------------

### Step 2: Run Exhaustive Algorithm Experiments

Edit `benchmark.py` and set:

``` python
n_values = [5, 10, 15, 20]
alpha = 1
trials = 3
```

Run:

``` bash
python benchmark.py
```

This benchmarks the exponential-time optimal solver for small input
sizes.

------------------------------------------------------------------------

### Step 3: Generate Plots

After collecting benchmark results, open `plots.py` and call the desired
plotting functions.

Run:

``` bash
python plots.py
```

This produces: - Runtime vs n (log--log scale) for greedy algorithms -
Normalized greedy runtime: t(n) / (n log₂ n) - Runtime vs n for
exhaustive algorithm

Save plots as PNG or PDF for the report.

------------------------------------------------------------------------

## Big-O Validation

### Greedy Algorithms

-   Plot runtime t(n) vs n (log--log scale)
-   Plot normalized runtime t(n) / (n log₂ n)
-   Normalized runtime approaches a constant

### Exhaustive Algorithm

-   Plot runtime t(n) vs n
-   Plot normalized runtime t(n) / (n·2ⁿ)
-   Runtime grows exponentially

------------------------------------------------------------------------

## Expected Results

-   EFT always produces an optimal solution
-   EST and SD may be suboptimal in high-overlap datasets
-   All greedy algorithms scale similarly
-   Exhaustive algorithm exhibits exponential growth
-   Normalized greedy runtime approaches a constant
-   Earliest Finish Time always matches the optimal solution
-   Other greedy strategies may be suboptimal under high overlap

------------------------------------------------------------------------

## Experimental Methodology

-   Dataset generation time excluded from measurements
-   High-resolution timers used
-   Warm-up run performed before timing
-   Mean and standard deviation reported

------------------------------------------------------------------------

## Requirements

-   Python 3.8+
-   numpy
-   matplotlib

------------------------------------------------------------------------

## Author

Yosakorn\
Advanced Algorithms & Data Structures\
Programming Assignment: Interval Scheduling
