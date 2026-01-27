#!/usr/bin/env python

# Number to guess: How many entries can we add to a dictionary of a fixed maximum size in a second?

# Entries: 50,000,000
# Time: 2.487682 seconds
# Rate: 20,099,035 entries/second

# Note: we take `i % 1000` to control the size of the dictionary


import time


def f(NUMBER: int) -> None:
    d = {}
    for i in range(NUMBER):
        d[i % 1000] = i


if __name__ == '__main__':
    import sys

    entries: int = int(sys.argv[1])

    start: float = time.perf_counter()
    f(entries)
    end: float = time.perf_counter()

    elapsed: float = end - start
    rate: float = entries / elapsed

    print(f"Entries: {entries:,}")
    print(f"Time: {elapsed:.6f} seconds")
    print(f"Rate: {rate:,.0f} entries/second")
