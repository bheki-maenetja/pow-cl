# Standard Library Imports
# Third Party Imports
from tabulate import tabulate
# Local Imports

# Get Search Table -- returns tabulated search data
def get_search_table(search_data):
  if len(search_data) == 0:
    print("No Matches. Try again!")
    return
  formatted_data = [{ key.upper(): obj[key] for key in obj } for obj in search_data]
  tabulated_data = tabulate(formatted_data, headers="keys", showindex=range(1, len(formatted_data) + 1))
  print(tabulated_data)