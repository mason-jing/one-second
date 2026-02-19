#!/usr/bin/env python

# Number to guess: How many passwords can we bcrypt in a second?

# Passwords: 20
# Time: 3.474833 seconds
# Rate: 6 passwords/second


import time

import bcrypt

password: bytes = b'a' * 72  # bcrypt max password length is 72 bytes


def f(NUMBER: int) -> None:
    for _ in range(NUMBER):
        bcrypt.hashpw(password, bcrypt.gensalt())


if __name__ == '__main__':
    import sys

    passwords: int = int(sys.argv[1])

    start: float = time.perf_counter()
    f(passwords)
    end: float = time.perf_counter()

    elapsed: float = end - start
    rate: float = passwords / elapsed

    print(f"Passwords: {passwords:,}")
    print(f"Time: {elapsed:.6f} seconds")
    print(f"Rate: {rate:,.0f} passwords/second")
