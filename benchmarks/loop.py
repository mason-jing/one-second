#!/usr/bin/env python

# Number to guess: How many iterations of an empty loop can we go through in a second?

# Iterations: 100,000,000
# Time: 1.414549 seconds
# Rate: 70,693,885 iterations/second


import time

def f(NUMBER):
    for _ in range(NUMBER):
        pass


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
