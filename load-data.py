import requests
import json
import re

api_url = "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/id/29.json"

data = requests.get(api_url)
json_data = data.json()

for i in json_data:
  if i == 'appearance':
    appearance = json_data[i].copy()
    appearance['height'] = f"{appearance['height'][1]} ({appearance['height'][0]})" 
    appearance['weight'] = f"{appearance['weight'][1]} ({appearance['weight'][0]})"
    appearance['eye_colour'] = appearance['eyeColor']
    appearance['hair_colour'] = appearance['hairColor'] if appearance['hairColor'] != "No Hair" else "n/a"
    del appearance['eyeColor'], appearance['hairColor']

    json_data[i] = { key : appearance[key].lower() if appearance[key] else "n/a" for key in appearance }
  elif i == 'biography':
    biography = json_data[i].copy()
    biography['full_name'] = biography['fullName'] if biography['fullName'] else "n/a"
    biography['place_of_birth'] = biography['placeOfBirth'] if biography['placeOfBirth'] != "-" else "n/a"
    biography['first_appearance'] = biography['firstAppearance'] if biography['firstAppearance'] != "-" else "n/a"
    biography['alter_egos'] = biography['alterEgos'] if biography['alterEgos'] != "No alter egos found." else "n/a"
    biography['aliases'] = [alias.lower() for alias in biography['aliases'] if alias != '-']
    del biography['fullName'], biography['placeOfBirth'], biography['firstAppearance'], biography['alterEgos']

    json_data[i] = { key : biography[key].lower() if key != 'aliases' else biography[key] for key in biography }
  elif i == 'work':
    work = json_data[i].copy()
    work['occupation'] = re.split(',|_|-|!|;', work['occupation']) if work['occupation'] != '-' else 'n/a'
    work['base'] = work['base'].lower() if work['base'] != "-" else "n/a"

    json_data[i] = { key: work[key] for key in work }


for i in json_data:
  print(i)
  print(json_data[i], end="\n\n")