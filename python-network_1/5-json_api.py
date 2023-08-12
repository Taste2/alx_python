"""
Python script that takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests

if sys.argv[1] == "":
    q = ""
else:
    q = sys.argv[1]

parameter = {'q':q}
url = 'http://0.0.0.0:5000/search_user'
response = requests.post(url, json=parameter)

if response.json():
    for key, value in response.json().items():
        print("[{}] {}".format(key, value))
elif not response.json():
    print("No result")
else:
    print("Not a valid JSON")