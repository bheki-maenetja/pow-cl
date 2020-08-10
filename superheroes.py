# Standard Library Imports
# Third-Party Imports
# Local Imports
from load_data import format_json, get_api_data

# Superhero Classes
class Superhero:
  hero_id = 0

  def __set_dict_attributes(self, obj_dict):
    for key in obj_dict:
      setattr(self, key, obj_dict[key])

  def __init__(self, name, image, powerstats, appearance={}, biography={}, connections={}, work={}):
    self._id = Superhero.hero_id
    self.name = name.lower()
    self.powerstats = powerstats
    self.image = image
    self.__appearance_attrs = list(appearance.keys())
    self.__biography_attrs = list(biography.keys())
    self.__connection_attrs = list(connections.keys())
    self.__work_attrs = list(work.keys())
    
    for _dict in (appearance, biography, connections, work):
      self.__set_dict_attributes(_dict)
    
    Superhero.hero_id += 1
 
  def __str__(self):
    return f"{self.name.title()} - (Id: {self._id})"
  
  def get_name(self):
    return self.name.lower()
  
  def get_id(self):
    return self._id
  
  def get_appearance(self):
    appearance_dict = {}
    for key in self.__appearance_attrs:
      appearance_dict[key] = getattr(self, key, 'n/a')
    return appearance_dict
    
  def get_biography(self):
    biography_dict = {}
    for key in self.__biography_attrs:
      biography_dict[key] = getattr(self, key, 'n/a')
    return biography_dict

  def get_connections(self):
    connection_dict = {}
    for key in self.__connection_attrs:
      connection_dict[key] = getattr(self, key, 'n/a')
    return connection_dict

  def get_work_details(self):
    work_dict = {}
    for key in self.__work_attrs:
      work_dict[key] = getattr(self, key, 'n/a')
    return work_dict

# Create a Superhero
def create_hero(hero_object):
  return Superhero(
    hero_object['name'], 
    hero_object['image'], 
    hero_object['powerstats'], 
    hero_object['appearance'], 
    hero_object['biography'], 
    hero_object['connections'], 
    hero_object['work']
  )

# Create the hero index
def get_hero_index(heroes):
  return { (hero.get_id(), hero.get_name()): hero for hero in heroes }

API_URL = "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/all.json"
API_DATA = get_api_data(API_URL)

# FORMATTED_OBJECTS = [format_json(json_object) for json_object in API_DATA]
SUPERHERO_OBJECTS = [create_hero(format_json(json_object)) for json_object in API_DATA]
HERO_INDEX = get_hero_index(SUPERHERO_OBJECTS)

print(HERO_INDEX)