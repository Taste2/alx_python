"""
 Python script that takes your GitHub credentials
   (username and password) and uses the GitHub API to display your id
"""
import sys 
import requests

url = 'https://api.github.com/user'
username = sys.argv[1]
password = sys.argv[2]

response = requests.get(url)
print(response.headers['id'])