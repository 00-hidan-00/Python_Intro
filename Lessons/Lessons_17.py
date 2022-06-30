# Безопасность проектов

import requests
import os
from requests_oauthlib import OAuth1
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# print(API_KEY, API_SECRET)

auth = OAuth1(API_KEY, API_SECRET)

endpoint = "http://api.thenounproject.com/icon/2"

response = requests.get(endpoint, auth=auth)
result = response.json()
# print(response.content)
icon_url = result["icon"]["icon_url"]

icon_response = requests.get(icon_url)

with open("test.svg", 'wb')as file:
    file.write(icon_response.content)