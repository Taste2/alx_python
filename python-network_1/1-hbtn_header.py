"""
This script takes URL as argument and display the X-Request-Id
"""
import sys
import requests

url = sys.argv[1]
req = requests.get(url)

print(req.headers['X-Request-Id'])