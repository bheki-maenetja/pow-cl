# Standard Library Imports
# Third-Party Imports
# Local Imports
from util.load_data import format_json, get_api_data

# Superhero Classes
class Superhero:
  hero_id = 0

  def __set_dict_attributes(self, obj_dict):
    for key in obj_dict:
      setattr(self, key, obj_dict[key])

  def __init__(self, name, image, powerstats, appearance={}, biography={}, connections={}, work={}):
    self._id = Superhero.hero_id
    self.name = name
    self.image = image
    self.powerstats = powerstats
    self.__appearance_attrs = list(appearance.keys())
    self.__biography_attrs = list(biography.keys())
    self.__connection_attrs = list(connections.keys())
    self.__work_attrs = list(work.keys())
    
    for _dict in (appearance, biography, connections, work):
      self.__set_dict_attributes(_dict)
    
    Superhero.hero_id += 1
 
  def __str__(self):
    return f"{self.name} - (Id: {self._id})"
  
  def get_id(self):
    return self._id

  def get_name(self):
    return self.name
  
  def get_image(self):
    return self.image

  def get_powerstats(self):
    return self.powerstats
  
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
  
  def get_all_info(self):
    return {
      'id': self.get_id(),
      'name': self.get_name(),
      'image': self.get_image(),
      'powerstats': self.get_powerstats(),
      'appearance': self.get_appearance(),
      'biography': self.get_biography(),
      'connections': self.get_connections(),
      'work': self.get_work_details(),
    }

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
def get_hero_index():
  try:
    api_data = get_api_data()
    heroes = [create_hero(format_json(json_object)) for json_object in api_data]
    return { (hero.get_id(), hero.get_name()): hero for hero in heroes }
  except:
    print("Something went wrong when loading the superheroes. Sorry!")
    return None


