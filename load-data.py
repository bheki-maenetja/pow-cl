import requests
import json

api_url = "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/id/167.json"

data = requests.get(api_url)
json_data = data.json()

for i in json_data:
  if i == 'appearance':
    appearance = json_data[i]
    appearance['height'] = f"{appearance['height'][1]} ({appearance['height'][0]})" 
    appearance['weight'] = f"{appearance['weight'][1]} ({appearance['weight'][0]})"
    appearance['eye_colour'] = appearance['eyeColor']
    del appearance['eyeColor']


for i in json_data:
  print(i)
  print(json_data[i])
  print()