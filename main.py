import requests
from dotenv import dotenv_values
import os
import sqlalchemy

api_key = dotenv_values(".env")

fred_url = f"https://api.stlouisfed.org/fred/category?category_id=125&api_key={api_key['key_fred']}&file_type=json"

header = {"Content-Type":"application/json", "Accept-Encoding":"deflate"}

response = requests.get(fred_url, headers=header)

responseData = response.json()
print(responseData)