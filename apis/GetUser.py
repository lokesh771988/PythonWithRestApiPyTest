import requests

url = "https://gorest.co.in/public/v2/users/108"

payload={}
headers = {
  'Authorization': 'Bearer 7232803c821bc49a0bd5c56d7df39c5289168e323fb17c5b6b1597d8941e33ef'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
