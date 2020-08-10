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


# my_first_hero = Superhero('The One', [1,2,3], {'xs': 'https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/167-century.jpg', 'sm': 'https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/167-century.jpg', 'md': 'https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/167-century.jpg', 'lg': 'https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/167-century.jpg'})

# print(my_first_hero)