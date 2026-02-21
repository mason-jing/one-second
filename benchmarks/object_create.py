#!/usr/bin/env python

# Number to guess: How many objects can we create in a second?

# Objects: 10,000,000
# Time: 2.479332 seconds
# Rate: 4,033,345 objects/second


import time


class MyObject(object):
    def __init__(self) -> None:
        self.a = 'a'
        self.b = 'b'
        self.c = 'a'
        self.d = 'b'
        self.e = 'a'
        self.f = 'b'
        self.g = 'a'
        self.h = 'b'
        self.i = 'a'
        self.j = 'b'
        self.k = 'a'
        self.l = 'b'
        self.m = 'a'
        self.n = 'b'
        self.o = 'a'
        self.p = 'b'
        self.q = 'a'
        self.r = 'b'
        self.s = 'a'
        self.t = 'b'
        self.u = 'a'
        self.v = 'b'
        self.w = 'b'
        self.x = 'b'
        self.y = 'b'
        self.z = 'b'


def f(NUMBER: int) -> None:
    for _ in range(NUMBER):
        MyObject()


if __name__ == '__main__':
    import sys

    objects: int = int(sys.argv[1])

    start: float = time.perf_counter()
    f(objects)
    end: float = time.perf_counter()

    elapsed: float = end - start
    rate: float = objects / elapsed

    print(f"Objects: {objects:,}")
    print(f"Time: {elapsed:.6f} seconds")
    print(f"Rate: {rate:,.0f} objects/second")
