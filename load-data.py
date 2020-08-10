import requests
import json
import re

api_url = "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/all.json"

data = requests.get(api_url)
json_data = data.json()

def format_json(json_data):
  json_data['image'] = json_data['images']['lg']
  del json_data['id'], json_data['slug'], json_data['images']

  for i in json_data:
    if i == 'appearance':
      appearance = json_data[i].copy()
      # print(appearance)
      appearance['height'] = f"{appearance['height'][1]} ({appearance['height'][0]})" if len(appearance['height']) == 2 else 'n/a'
      appearance['weight'] = f"{appearance['weight'][1]} ({appearance['weight'][0]})"
      appearance['eye_colour'] = appearance['eyeColor']
      appearance['hair_colour'] = appearance['hairColor'] if appearance['hairColor'] != "No Hair" else "n/a"
      del appearance['eyeColor'], appearance['hairColor']

      json_data[i] = { key : appearance[key].lower() if appearance[key] and appearance[key] != '-' else "n/a" for key in appearance }
    elif i == 'biography':
      biography = json_data[i].copy()
      biography['full_name'] = biography['fullName'] if biography['fullName'] else "n/a"
      biography['place_of_birth'] = biography['placeOfBirth'] if biography['placeOfBirth'] != "-" else "n/a"
      biography['first_appearance'] = biography['firstAppearance'] if biography['firstAppearance'] != "-" else "n/a"
      biography['alter_egos'] = biography['alterEgos'] if biography['alterEgos'] != "No alter egos found." else "n/a"
      aliases = [alias.lower() for alias in biography['aliases']] if biography['aliases'] != ['-'] else 'n/a'
      del biography['fullName'], biography['placeOfBirth'], biography['firstAppearance'], biography['alterEgos'], biography['aliases']

      json_data[i] = { key : biography[key].lower() if biography[key] and biography[key] != '-' else 'n/a' for key in biography }
      json_data[i]['aliases'] = aliases
    elif i == 'work':
      work = json_data[i].copy()
      work['occupation'] = [word.strip().lower() for word in re.split(',|_|-|!|;', work['occupation'])] if work['occupation'] != '-' else 'n/a'
      work['base'] = work['base'].lower() if work['base'] != "-" else "n/a"

      json_data[i] = { key: work[key] for key in work }
    elif i == 'connections':
      connections = json_data[i].copy()
      connections['group_affiliations'] = [word.strip().lower() for word in re.split(',|_|-|!|;', connections['groupAffiliation'])] if connections['groupAffiliation'] != '-' else 'n/a'
      connections['relatives'] = [word.strip().lower() for word in re.split(',|_|-|!|;', connections['relatives'])] if connections['relatives'] != '-' else 'n/a'
      del connections['groupAffiliation']

      json_data[i] = connections
  
  return json_data

formatted_objects = [format_json(json_object) for json_object in json_data]
for data_object in formatted_objects:
  print(data_object, end="\n\n")