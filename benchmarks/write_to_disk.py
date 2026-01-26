#!/usr/bin/env python

# Number to guess: How many bytes can we write to an output file in a second?
# Note: we make sure everything is sync'd to disk before exiting :)

# Iterations: 1,000,000,000
# Time: 1.320435 seconds
# Rate: 757,326,012 iterations/second


import time
from os import fsync, remove
from typing import TextIO

CHUNK_SIZE: int = 1000000
s: str = "a" * CHUNK_SIZE


def cleanup(fh: TextIO, name: str) -> None:
    fh.flush()
    fsync(fh.fileno())
    fh.close()
    try:
        remove(name)
    except:
        pass


def f(NUMBER: int) -> None:
    name: str = './out'
    file_handle: TextIO = open(name, 'w')
    bytes_written: int = 0
    while bytes_written < NUMBER:
        file_handle.write(s)
        bytes_written += CHUNK_SIZE
    cleanup(file_handle, name)


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
