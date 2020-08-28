# Standard Library Imports
from subprocess import call
from json import dumps
from os import path
# Third Party Imports
# Local Imports
from util.util_functions import get_string, get_integer, get_bool, user_prompts
from search.search_table import get_search_table

# Search Handler - handles navigation of search functionality
def handle_search(index, display_all=False):
  user_input = get_string(user_prompts['search-heroes'], min_length=1) if not display_all else ""
  while True:
    if user_input == '0':
      break
    elif user_input == "" and display_all: # Get all heroes - returns all the heroes in a search table
      search_results = simple_search(index)
      get_search_table(search_results)
      super_hero = get_hero(search_results, index)
      if super_hero:
        input("<DISPLAY HERO/>")
        save_hero(super_hero)
        call(path.join(path.dirname(__file__), "../bash_scripts/display_hero.sh"), shell=True)
      display_all = False
    else:
      search_results = simple_search(index, user_input)
      get_search_table(search_results)
      if len(search_results) > 0:
        super_hero = get_hero(search_results, index)
        if super_hero: 
          input("<DISPLAY HERO/>")
          save_hero(super_hero)
          call(path.join(path.dirname(__file__), "../bash_scripts/display_hero.sh"), shell=True)
    user_input = get_string(user_prompts['search-heroes'], min_length=1)

# Create a single row of search results
def create_row(hero_obj, add_appearance=False):
  new_dict = {}
  new_dict['id'] = hero_obj.get_id()
  new_dict['name'] = hero_obj.get_name().title()
  if add_appearance: 
    new_dict.update(hero_obj.get_appearance())
  new_dict.update(hero_obj.get_powerstats())
  return new_dict

# Simple Search - search for heroes by name
def compare_string(search_term, value):
  if search_term == value:
    return True
  else:
    return search_term in value or value in search_term

def simple_search(index, search_name=""):
  sort_by_overall = get_bool(user_prompts['explore-heroes-sort'])
  additional_info = get_bool(user_prompts['explore-heroes-info'])
  search_results = [create_row(hero, additional_info) for hero in index.values() if not search_name or compare_string(search_name.lower(), hero.get_name())]
  if sort_by_overall:
    search_results.sort(key=lambda hero: hero['overall'], reverse=True)
  else:
    search_results.sort(key=lambda hero: hero['name'])
  return search_results

# Get hero - view a single hero from the search results
def get_hero(search_results, index):
  choice_index = get_integer(user_prompts['get-heroes'], len(search_results), 1, 'b')
  if not choice_index:
    return None
  chosen_hero = search_results[choice_index - 1]
  return next( index[key] for key in index if key[0] == chosen_hero['id'] )

# Select hero - select a hero object and store its information in the current_hero file
def save_hero(hero_obj):
  hero_data = hero_obj.get_all_info()
  hero_json_data = dumps(hero_data)
  try:
    file_handler = open(path.join(path.dirname(__file__), "../display/current_hero.txt"), 'w')
    file_handler.write(hero_json_data)
  except:
    print('Something went wrong')




