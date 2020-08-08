import requests
import json

api_url = "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/id/1.json"

data = requests.get(api_url)
json_data = data.json()

for i in json_data:
  if i == 'appearance':
    appearance = json_data[i]
    appearance['height'] = f"{appearance['height'][1]} ({appearance['height'][0]})" 
    appearance['weight'] = f"{appearance['weight'][1]} ({appearance['weight'][0]})"
    appearance['eye_colour'] = appearance['eyeColor']
    appearance['hair_colour'] = appearance['hairColor'] if appearance['hairColor'] != "No Hair" else "n/a"
    del appearance['eyeColor']
    del appearance['hairColor']

    for key in appearance:
      appearance[key] = appearance[key].lower()
  elif i == 'biography':
    biography = json_data[i]
    biography['full_name'] = biography['fullName'] if biography['fullName'] else "n/a"
    del biography['fullName']


for i in json_data:
  print(i)
  print(json_data[i], end="\n\n")