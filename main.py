# Standard Library Imports
from util import get_integer, get_string

# Third-party Imports
from tabulate import tabulate

# Local Imports
from superheroes import get_hero_index
from search import simple_search

# THE MAIN FUNCTION
def main():
  """
  PARAMETERS -> None
  RETURN VALUES -> None

  HOW IT WORKS
  ------------
  1) Facilitates the functionality of the search & comparison tools
  2) Provides the user interface
  """
  input("Welcome to POW!!! Your #1 place for all things superhero >>> ")

  print("Loading superheroes...")
  hero_index = get_hero_index()

  user_prompts = {
    "general": "To explore your favourite superheroes, press 'e'. If you want to search for a particular hero press 's'. Or you can check out our nifty comparison tool; just press 'c'. To quit press 'q'",
    "general-error": "Please enter a valid input"
  }

  while hero_index:
    user_input = get_string(1,1, user_prompts["general"], user_prompts["general-error"], accept_values=['e', 's', 'c', 'q'])
    if user_input == 'q':
      break
    elif user_input == 'e':
      input("<EXPLORE HEROES/>")
    elif user_input == 's':
      input("<SEARCH FOR HERO/>")
      search_data = simple_search(hero_index)
      search_data.sort(key=lambda hero: hero["name"], reverse=True)
      search_table = tabulate(search_data, headers="keys", showindex=range(1, len(search_data) + 1))
      print(search_table)
    elif user_input == 'c':
      input("<COMPARISON TOOL/>")
  
  input("Thank you for using POW!!! >>> ")

if __name__ == "__main__":
    main()

