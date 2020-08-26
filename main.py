# Standard Library Imports
# from util import get_string, user_prompts
from util.util_functions import get_string, user_prompts

# Third-party Imports
# Local Imports
from superheroes.superhero_classes import get_hero_index
from search.search_handler import handle_search

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

  while hero_index:
    user_input = get_string(user_prompts["general"], 1, 1, accept_values=['e', 's', 'c', 'q'])
    if user_input == 'q':
      break
    elif user_input == 'e':
      input("<EXPLORE HEROES/>")
      handle_search(hero_index, display_all=True)
    elif user_input == 's':
      input("<SEARCH FOR HERO/>")
      handle_search(hero_index)
    elif user_input == 'c':
      input("<COMPARISON TOOL/>")
  
  input("Thank you for using POW!!! >>> ")

if __name__ == "__main__":
    main()

