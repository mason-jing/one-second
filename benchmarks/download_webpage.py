#!/usr/bin/env python

# Number to guess: How many times can we download google.com in a second?

# Downloads: 10
# Time: 2.454081 seconds
# Rate: 4 downloads/second


import time
from urllib.request import urlopen


def f(NUMBER: int) -> None:
    for _ in range(NUMBER):
        r = urlopen("https://google.com")
        r.read()


if __name__ == '__main__':
    import sys

    downloads: int = int(sys.argv[1])

    start: float = time.perf_counter()
    f(downloads)
    end: float = time.perf_counter()

    elapsed: float = end - start
    rate: float = downloads / elapsed

    print(f"Downloads: {downloads:,}")
    print(f"Time: {elapsed:.6f} seconds")
    print(f"Rate: {rate:,.0f} downloads/second")
