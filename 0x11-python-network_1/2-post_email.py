#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    URL = sys.argv[1]
    ENTRY = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(ENTRY).encode("ascii")

    Req = urllib.request.Request(URL, data)
    with urllib.request.urlopen(Req) as response:
        print(response.read().decode("utf-8"))
