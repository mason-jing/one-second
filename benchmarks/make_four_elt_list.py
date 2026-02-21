#!/usr/bin/env python


# Number to guess: How many four-element lists can we make in a second?

# Lists: 100,000,000
# Time: 4.104362 seconds
# Rate: 24,364,325 lists/second


import time


def f(NUMBER: int) -> None:
    for _ in range(NUMBER):
        [0, 1, 2, 3]


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
