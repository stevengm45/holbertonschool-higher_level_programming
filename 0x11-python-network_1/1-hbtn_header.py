#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL
    and displays the value """
import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print(response.info().get("X-Request-Id"))
