import requests

url = "http://developer.shopclues.com/api/v1/upload"

payload={}
files=[
  ('fileName',('Resume_Lokesh.docx',open('/C:/Users/GorantlL/Downloads/Resume_Lokesh.docx','rb'),'application/vnd.openxmlformats-officedocument.wordprocessingml.document'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
