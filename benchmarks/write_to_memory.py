#!/usr/bin/env python

# Number to guess: How many bytes can we write to a string in memory in a second?

# Bytes: 2,000,000,000
# Time: 1.155849 seconds
# Rate: 1,730,330,276 bytes/second


import time
from io import StringIO

CHUNK_SIZE: int = 1000000
s: str = "a" * CHUNK_SIZE


def f(NUMBER: int) -> None:
    output: StringIO = StringIO()
    bytes_written: int = 0
    while bytes_written < NUMBER:
        output.write(s)
        bytes_written += CHUNK_SIZE


if __name__ == '__main__':
    import sys

    num_bytes: int = int(sys.argv[1])

    start: float = time.perf_counter()
    f(num_bytes)
    end: float = time.perf_counter()

    elapsed: float = end - start
    rate: float = num_bytes / elapsed

    print(f"Bytes: {num_bytes:,}")
    print(f"Time: {elapsed:.6f} seconds")
    print(f"Rate: {rate:,.0f} bytes/second")
