# Standard Library Imports
from math import inf
# Third Party Imports
# Local Imports

# User Prompts
user_prompts = {
    "general": "To explore your favourite superheroes, press 'e'. If you want to search for a particular hero press 's'. Or you can check out our nifty comparison tool; just press 'c'. To quit press 'q'",
    "explore-heroes-info": "Would you like to view additional information about your heroes?",
    "explore-heroes-sort": "Would you like to sort your heroes by the their power levels?",
    "search-heroes": "Search for your favourite superhero or press 0 to go back",
    "get-heroes": "To view a hero enter it's corresponding number or press b to go back"
  }

# User Input
def get_integer(input_prompt, max_value, min_value, break_value):
  while True:
    try:
      number = input(f"{input_prompt}: ")
      if number == break_value:
        return None
      number = int(number)
      if int(number) not in range(min_value, max_value + 1): 
        raise ValueError
    except ValueError:
      print(f"Please enter a number between {min_value} and {max_value}! Or press {break_value} to go back.")
    else:
      break
  
  return number

def get_string(input_prompt, error_prompt="Please enter a valid input", max_length=inf, min_length=0, accept_values=None):
  user_error = False
  while True:
    try:
      string = input(f"{input_prompt if not user_error else error_prompt}: ").lower()
      if accept_values != None:
        if string not in accept_values: raise ValueError
      if len(string) > max_length or len(string) < min_length: raise ValueError
    except ValueError:
      user_error = True
    else:
      break
  
  return string

def get_bool(input_prompt, error_prompt="Please enter a valid input"):
  choice = get_string(f"{input_prompt} [y/n]", error_prompt, accept_values=['y', 'n'])
  if choice == 'y':
    return True
  elif choice == 'n':
    return False
