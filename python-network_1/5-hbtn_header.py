#!/usr/bin/python3
"""Fetches the value of X-Request-Id from the response header."""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
