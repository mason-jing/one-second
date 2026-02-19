#!/usr/bin/env python

# Number to guess: How many bytes can we md5sum in a second?

# Bytes: 2,000,000,000
# Time: 1.939694 seconds
# Rate: 1,031,090,737 bytes/second


import hashlib
import time

from _hashlib import HASH

CHUNK_SIZE: int = 10000
s: bytes = b'a' * CHUNK_SIZE


def f(NUMBER: int) -> None:
    bytes_hashed: int = 0
    h: HASH = hashlib.md5()
    while bytes_hashed < NUMBER:
        h.update(s)
        bytes_hashed += CHUNK_SIZE
    h.digest()


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
