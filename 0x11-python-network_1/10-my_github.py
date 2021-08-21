#!/usr/bin/python3
""" This script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get("https://api.github.com/user",
                            auth=requests.auth.HTTPBasicAuth(argv[1], argv[2]))
    try:
        text = response.json()
        print(text.get('id'))
    except:
        print("Not a valid JSON")
