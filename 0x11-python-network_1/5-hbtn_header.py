#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    URL = sys.argv[1]

    req = requests.get(URL)
    print(req.headers.get("X-Request-Id"))
