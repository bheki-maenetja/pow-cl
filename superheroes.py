class Superhero:
  id = 0

  def __init__(self, name, powerstats, image_url):
    self.name = name.lower()
    self.powerstats = powerstats
    self.image_url = image_url