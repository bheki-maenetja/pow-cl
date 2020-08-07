class Superhero:
  id = 0

  def __init__(self, name, powerstats, images):
    self.name = name.lower()
    self.powerstats = powerstats
    for key in images:
      setattr(self, key, images[key])
    
  def __str__(self):
    return self.name.title()


my_first_hero = Superhero('The One', [1,2,3], {'xs': 'https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/167-century.jpg', 'sm': 'https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/167-century.jpg', 'md': 'https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/167-century.jpg', 'lg': 'https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/167-century.jpg'})

print(my_first_hero)