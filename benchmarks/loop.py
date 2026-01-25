#!/usr/bin/env python

# Number to guess: How many iterations of an empty loop can we go through in a second?

# Iterations: 100,000,000
# Time: 1.414549 seconds
# Rate: 70,693,885 iterations/second


import time


def f(NUMBER: int) -> None:
    for _ in range(NUMBER):
        pass


if __name__ == '__main__':
    import sys

    iterations: int = int(sys.argv[1])

    start: float = time.perf_counter()
    f(iterations)
    end: float = time.perf_counter()

    elapsed: float = end - start
    rate: float = iterations / elapsed

    print(f"Iterations: {iterations:,}")
    print(f"Time: {elapsed:.6f} seconds")
    print(f"Rate: {rate:,.0f} iterations/second")
