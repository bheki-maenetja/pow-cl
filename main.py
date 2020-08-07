from util import get_integer, get_string

def main():
  """
  PARAMETERS -> None
  RETURN VALUES -> None

  HOW IT WORKS
  ------------
  1) Facilitates the functionality of the search tool
  2) Provides the user interface
  """
  input("Welcome to POW!!! Your #1 place for all things superhero >>> ")
  user_prompts = {
    "general": "To explore your favourite superheroes, press 'e'. If you want to search for a particular hero press 's'. Or you can check out our nifty comparison tool; just press 'c'. To quit press 'q'"
  }

  while True:
    user_input = get_string(1,1, user_prompts["general"], "Please enter a valid input", accept_values=['e', 's', 'c', 'q'])
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
