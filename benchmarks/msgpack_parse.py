#!/usr/bin/env python

# Number to guess: How many times can we parse 46KB of msgpack data in a second?

# Iterations: 5,000
# Time: 1.231749 seconds
# Rate: 4,059 iterations/second


import time
from pathlib import Path

import msgpack

# Get the path relative to this script's location
script_dir = Path(__file__).parent.parent
msgpack_path = script_dir / 'setup' / 'protobuf' / 'message.msgpack'

with open(msgpack_path, 'rb') as f:
    message = f.read()


def f(NUMBER: int) -> None:
    for _ in range(NUMBER):
        msgpack.unpackb(message)


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
