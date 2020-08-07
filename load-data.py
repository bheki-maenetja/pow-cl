import requests
import json

api_url = "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/id/1.json"

data = requests.get(api_url)
json_data = data.json()

for i in json_data:
  print(i)