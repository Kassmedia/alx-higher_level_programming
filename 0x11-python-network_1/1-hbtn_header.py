#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request


if __name__ == "__main__":
    URL = sys.argv[1]

    check = urllib.request.Request(URL)
    with urllib.request.urlopen(check) as response:
        print(dict(response.headers).get("X-Request-Id"))
