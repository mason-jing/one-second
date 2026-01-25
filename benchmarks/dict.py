#!/usr/bin/env python

# Number to guess: How many entries can we add to a dictionary of a fixed maximum size in a second?

# Iterations: 50,000,000
# Time: 2.487682 seconds
# Rate: 20,099,035 iterations/second

# Note: we take `i % 1000` to control the size of the dictionary


import time

def f(NUMBER):
    d = {}
    for i in range(NUMBER):
        d[i % 1000] = i


if __name__ == '__main__':
    import sys

    iterations = int(sys.argv[1])

    start = time.perf_counter()
    f(iterations)
    end = time.perf_counter()

    elapsed = end - start
    rate = iterations / elapsed

    print(f"Iterations: {iterations:,}")
    print(f"Time: {elapsed:.6f} seconds")
    print(f"Rate: {rate:,.0f} iterations/second")