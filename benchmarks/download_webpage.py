#!/usr/bin/env python

# Number to guess: How many times can we download google.com in a second?

# Iterations: 10
# Time: 2.454081 seconds
# Rate: 4 iterations/second


import time
from urllib.request import urlopen


def f(NUMBER: int) -> None:
    for _ in range(NUMBER):
        r = urlopen("https://google.com")
        r.read()


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
