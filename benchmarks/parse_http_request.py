#!/usr/bin/env python

# Number to guess: How many HTTP requests can we parse in a second?

# Requests: 100,000
# Time: 2.446060 seconds
# Rate: 40,882 requests/second


import time
from http.server import BaseHTTPRequestHandler
from io import BytesIO, BufferedIOBase
from typing import Optional


class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, request_text: str) -> None:
        self.rfile: BufferedIOBase = BytesIO(request_text.encode('utf-8'))
        self.raw_requestline: bytes = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self, code: int, message: Optional[str] = None) -> None:
        self.error_code: Optional[int] = code
        self.error_message: Optional[str] = message


request_text: str = """GET / HTTP/1.1
Host: localhost:8001
Connection: keep-alive
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en-GB,en-US;q=0.8,en;q=0.6
"""


def f(NUMBER: int) -> None:
    for _ in range(NUMBER):
        HTTPRequest(request_text)


if __name__ == '__main__':
    import sys

    requests: int = int(sys.argv[1])

    start: float = time.perf_counter()
    f(requests)
    end: float = time.perf_counter()

    elapsed: float = end - start
    rate: float = requests / elapsed

    print(f"Requests: {requests:,}")
    print(f"Time: {elapsed:.6f} seconds")
    print(f"Rate: {rate:,.0f} requests/second")
