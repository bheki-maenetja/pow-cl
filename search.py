# Standard Library Imports
# Third Party Imports
# Local Imports
from util import get_string, get_bool, user_prompts
from display import get_search_table

# Search Handler - handles navigation of search functionality
def handle_search(index):
  user_input = get_string("Enter the name of a superhero or press 0 to quit", "Please enter a valid input")
  while True:
    if user_input == '0':
      break
    else:
      search_results = simple_search(index, user_input, False)
      get_search_table(search_results)
    user_input = get_string("Enter the name of a superhero or press 0 to quit", "Please enter a valid input")

# Create a single row of search results
def create_row(hero_obj, add_appearance=False):
  new_dict = {}
  new_dict['name'] = hero_obj.get_name().title()

  if add_appearance: new_dict.update(hero_obj.get_appearance())

  new_dict.update(hero_obj.get_powerstats())
  return new_dict

# Simple Search - search for heroes by name
def compare_string(search_term, value):
  if search_term == value:
    return True
  else:
    return search_term in value or value in search_term

def simple_search(index, search_name="", additional_info=False, sort_by_overall=False):
  search_results = [create_row(hero, additional_info) for hero in index.values() if not search_name or compare_string(search_name.lower(), hero.get_name())]
  if sort_by_overall:
    search_results.sort(key=lambda hero: hero['overall'], reverse=True)
  else:
    search_results.sort(key=lambda hero: hero['name'])
  return search_results

# Get all heroes - returns all the heroes in a search table
def get_all_heroes(index):
  sort_by_power = get_bool(user_prompts['explore-heroes-sort'], user_prompts['general-error'])
  view_additional_info = get_bool(user_prompts['explore-heroes-info'], user_prompts['general-error'])
  get_search_table(simple_search(index, additional_info=view_additional_info, sort_by_overall=sort_by_power))


