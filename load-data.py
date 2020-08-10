import requests
import json
import re

from superheroes import Superhero

# Get JSON API response data
def get_api_data(url):
  data = requests.get(url)
  json_data = data.json()
  return json_data

# Formatting JSON API response data
def format_json(json_data):
  json_data['image'] = json_data['images']['lg']
  del json_data['id'], json_data['slug'], json_data['images']

  for i in json_data:
    if i == 'powerstats':
      powerstats = json_data[i].copy()
      powerstats['overall'] = round( sum(powerstats[i] for i in powerstats) / len(powerstats) )
      json_data[i] = powerstats
    elif i == 'appearance':
      appearance = json_data[i].copy()
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

# Creating Superhero Objects from the Superhero Class
def create_hero(hero_object):
  return Superhero(
    hero_object['name'], 
    hero_object['image'], 
    hero_object['powerstats'], 
    hero_object['appearance'], 
    hero_object['biography'], 
    hero_object['connections'], 
    hero_object['work']
  )

# Create the hero index
def get_hero_index(heroes):
  pass


API_URL = "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/all.json"
API_DATA = get_api_data(API_URL)

FORMATTED_OBJECTS = [format_json(json_object) for json_object in API_DATA]
SUPERHERO_OBJECTS = [create_hero(hero_object) for hero_object in FORMATTED_OBJECTS]

for superhero in SUPERHERO_OBJECTS:
  print(superhero, superhero.powerstats, sep='\n')
