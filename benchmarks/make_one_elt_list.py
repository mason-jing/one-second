#!/usr/bin/env python


# Number to guess: How many one-element lists can we make in a second?

# Lists: 100,000,000
# Time: 3.542389 seconds
# Rate: 28,229,533 lists/second


import time


def f(NUMBER: int) -> None:
    for _ in range(NUMBER):
        [0]


if __name__ == '__main__':
    import sys

    lists: int = int(sys.argv[1])

    start: float = time.perf_counter()
    f(lists)
    end: float = time.perf_counter()

    elapsed: float = end - start
    rate: float = lists / elapsed

    print(f"Lists: {lists:,}")
    print(f"Time: {elapsed:.6f} seconds")
    print(f"Rate: {rate:,.0f} lists/second")
