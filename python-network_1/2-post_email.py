"""
 Python script that takes in a URL and an email address
"""
import sys
import requests

url = sys.argv[1]
email = {'email':sys.argv[2]}


response = requests.post(url, params=email)
print(response.text)

