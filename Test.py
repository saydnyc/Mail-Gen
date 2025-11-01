import requests
import random
import string

url = "https://1sec-mail.com/get_messages"

Token = ""
Data = {}
Response = {}
Session = {}

def GenerateSession():
    Session = requests.Session()

def GenerateToken():
    characters = string.ascii_letters + string.digits
    Token = ''.join(random.choice(characters) for _ in range(30))
    return Token

def GenerateData():
    Data = {"_token": Token,}
    return Data

def GetResponse():
    Response = Session.post(url, data=Data)
    return Response
