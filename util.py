# Standard Library Imports
from math import inf
# Third Party Imports
# Local Imports

# User Prompts
user_prompts = {
    "general": "To explore your favourite superheroes, press 'e'. If you want to search for a particular hero press 's'. Or you can check out our nifty comparison tool; just press 'c'. To quit press 'q'",
    "explore-heroes-info": "Would you like to view your heroes with additional information?",
    "explore-heroes-sort": "Would you like to sort your heroes by the their power levels?"
  }

# User Input
def get_integer(min_value, max_value, input_prompt):
  while True:
    try:
      number = int(input(f"{input_prompt}: "))
      if number not in range(min_value, max_value + 1): raise ValueError
    except ValueError:
      print(f"Please enter a number between {min_value} and {max_value}!!!")
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
