# Безопасность проектов

import requests
import os
from requests_oauthlib import OAuth1
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")



print(API_KEY,API_SECRET)

auth = OAuth1(API_KEY, API_SECRET)

endpoint = "http://api.thenounproject.com/icon/1"

response = requests.get(endpoint, auth=auth)
print(response.content)
