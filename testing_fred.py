import requests
#import json

fred_url = "https://api.stlouisfed.org/fred/category?category_id=125&api_key=319a37d839ed97a78733ef2be4d24da4&file_type=json"

response = requests.get(fred_url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)

