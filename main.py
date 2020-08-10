# Standard Library Imports
from util import get_integer, get_string

# Third-party Imports

# Local Imports
from superheroes import get_hero_index

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
    elif user_input == 'c':
      input("<COMPARISON TOOL/>")
  
  input("Thank you for using POW!!! >>> ")

if __name__ == "__main__":
    main()

