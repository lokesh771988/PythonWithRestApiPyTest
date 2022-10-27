import requests
import json

url = "https://gorest.co.in/public/v2/users"

payload = json.dumps({
  "name": "Tenali Ramakrishna3",
  "gender": "male",
  "email": "tenali.ramakrishna3@15ce.com",
  "status": "active"
})
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer 7232803c821bc49a0bd5c56d7df39c5289168e323fb17c5b6b1597d8941e33ef'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
