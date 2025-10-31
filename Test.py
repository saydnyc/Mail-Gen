import requests
import random
import string

url = "https://1sec-mail.com/get_messages"

def GenerateToken():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(30))

def GenerateData():
    token = GenerateToken()
    return {"_token": token,}

response = requests.post(url, data=GenerateData())
print(response.status_code)
print(response.text)