#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import sys
import requests


if __name__ == "__main__":
    message = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": message}

    req = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
