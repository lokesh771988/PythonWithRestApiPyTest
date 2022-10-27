import requests

url = "https://postman-echo.com/basic-auth"

payload={}
headers = {
  'Authorization': 'Basic cG9zdG1hbjpwYXNzd29yZA=='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
