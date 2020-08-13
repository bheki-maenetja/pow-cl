# Standard Library Imports
# Third Party Imports
# Local Imports
from util import get_string

# Search Handler - handles navigation of search functionality
def handle_search():
  pass

# Create a single row of search results
def create_row(hero_obj, add_appearance=False, add_bio=False, add_work=False):
  new_dict = {}
  new_dict['name'] = hero_obj.get_name().title()

  if add_appearance: hero_obj.update(hero_obj.get_appearance())
  if add_bio: hero_obj.update(hero_obj.get_biography())
  if add_work: hero_obj.update(hero_obj.get_work_details())

  new_dict.update(hero_obj.get_powerstats())
  return new_dict

# Simple Search - search for heroes by name
def simple_search(index, search_name=""):
  search_results = [create_row(hero) for hero in index.values() if hero.get_name() in search_name or search_name in hero.get_name()]
  return search_results


