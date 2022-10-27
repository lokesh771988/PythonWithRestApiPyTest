import requests

url = "https://gorest.co.in/public/v2/users?page=1"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
