import requests
import json

url = "http://hackathons.masterschool.com:3030/sms/send"
headers = {
        'Content-Type': 'application/json'
    }
body = {
  "apiToken": "ff5545473ee5ccf545e77dd52ed2a62e-6e416a63-6fa1-414a-80b6-d784479d61c8",
  "baseUrl": "https://v36qlv.api.infobip.com",
  "phoneNumber": 491788580904,
  "message": "Hello, this is a test message from your terminal!",
  "sender": "TooneyTunes"
}

requests.post(url, headers=headers, data=json.dumps(body))