# Standard Library Imports
# Third Party Imports
# Local Imports
from util import get_string
from display import get_search_table

# Search Handler - handles navigation of search functionality
def handle_search(index):
  user_input = get_string("Enter the name of a superhero or press 0 to quit", "Please enter a valid input")
  while True:
    if user_input == '0':
      break
    else:
      search_results = simple_search(index, user_input)
      get_search_table(search_results)
    user_input = get_string("Enter the name of a superhero or press 0 to quit", "Please enter a valid input")

# Create a single row of search results
def create_row(hero_obj, add_appearance=False, add_work=False):
  new_dict = {}
  new_dict['name'] = hero_obj.get_name().title()

  if add_appearance: new_dict.update(hero_obj.get_appearance())

  new_dict.update(hero_obj.get_powerstats())
  return new_dict

# Simple Search - search for heroes by name
def simple_search(index, search_name=""):
  search_results = [create_row(hero, True) for hero in index.values() if hero.get_name() in search_name or search_name in hero.get_name()]
  return search_results


