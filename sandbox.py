import requests
import json

api_url = "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/1.json"

data = requests.get(api_url)

json_data = json.loads(data)
print(json_data)