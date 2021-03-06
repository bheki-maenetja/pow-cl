# Standard Library Imports
from sys import argv
from os import path
from json import loads
import io
from urllib.request import urlopen
from random import choice

# Third-Party imports
import pygame

# Local Imports
import colours

# Button Sprites - spirites that represent buttons on a screen
class Button(pygame.sprite.Sprite):
  def __init__(self, x, y, width, height, text, font_size, is_selected=False):
    super(Button, self).__init__()
    self.image = pygame.Surface((width, height))

    if is_selected:
      self.image.fill(colours.WHITE)
      draw_text(self.image, text, font_size, width // 2, height // 2, font_colour=colours.BLACK, align_centre=True)
    else:
      self.image.fill(colours.BLACK)
      draw_text(self.image, text, font_size, width // 2, height // 2, font_colour=colours.WHITE, align_centre=True)
    self.rect = self.image.get_rect(center=(x, y))
    self.width = width
    self.height = height
    self.text = text
    self.font_size = font_size
    self.is_selected = is_selected
  
  def get_rect(self):
    return self.rect
  
  def get_text(self):
    return self.text
  
  def is_button_selected(self):
    return self.is_selected

  def select_button(self):
    self.is_selected = True
    self.image.fill(colours.WHITE)
    draw_text(self.image, self.text, self.font_size, self.width // 2, self.height // 2, font_colour=colours.BLACK, align_centre=True)
  
  def de_select_button(self):
    self.is_selected = False
    self.image.fill(colours.BLACK)
    draw_text(self.image, self.text, self.font_size, self.width // 2, self.height // 2, font_colour=colours.WHITE, align_centre=True)

# Display hero - display the hero's picture along with all their info
def display_hero():
  WIDTH, HEIGHT = 540, 720
  BACKGROUND_COLOUR = choice((colours.ORANGE, colours.YELLOW, colours.GREEN))
  FPS = 30
  
  hero_data = load_hero_data()
  hero_image = load_hero_image(hero_data['image'])
  
  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  clock = pygame.time.Clock()

  bio_button = Button(54, 480, 90, 40, 'Biography', 23, is_selected=True)
  appearance_button = Button(162, 480, 90, 40, 'Appearance', 20)
  work_button = Button(270, 480, 90, 40, 'Work', 25)
  connections_button = Button(378, 480, 90, 40, 'Connections', 20)
  powerstats_button = Button(486, 480,90, 40, 'Powerstats', 20)

  buttons = pygame.sprite.Group()

  buttons.add(bio_button)
  buttons.add(appearance_button)
  buttons.add(work_button)
  buttons.add(connections_button)
  buttons.add(powerstats_button)

  # GAME LOOP
  running = True

  while running:
    # Process Input (events)
    for event in pygame.event.get():
      if event.type == pygame.QUIT: # check for closing the window
        running = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        for button in buttons:
          if button.get_rect().collidepoint(x,y):
            for i in buttons: 
              i.de_select_button()
            button.select_button()

    # Update
    # Draw / Render
    screen.fill(BACKGROUND_COLOUR)
    screen.blit(hero_image, (WIDTH // 2 - 150, 10))
    draw_text(screen, hero_data['name'], 36, WIDTH // 2, 435, align_centre=True)
    buttons.draw(screen)
    selected_button = next(button for button in buttons if button.is_button_selected())
    render_hero_info(screen, hero_data[selected_button.get_text().lower()])
    # AFTER Drawing Everything, Flip the Display
    pygame.display.flip()

    # Keep Game Loop Running at Given FPS
    clock.tick(FPS)

# Load hero info - loads hero information from the current_hero file
def load_hero_data():
  try:
    file_handler = open(path.join(path.dirname(__file__), argv[1]), 'r')
    data = next(line for line in file_handler.readlines())
    hero_data = loads(data)
    return hero_data
  except:
    print('Could not load hero info')

def load_hero_image(image_url):
  image_str = urlopen(image_url).read()
  image_file = io.BytesIO(image_str)
  hero_image = pygame.image.load(image_file)
  return pygame.transform.scale(hero_image, (300,400))

# Text handling - writes text on the pygame window
def draw_text(surf, text, font_size, x, y, font_name='arial', font_colour=colours.BLACK, align_centre=False):
  chosen_font = pygame.font.match_font(font_name)
  font = pygame.font.Font(chosen_font, font_size)
  text_surf = font.render(text, True, font_colour)
  text_rect = text_surf.get_rect()
  if align_centre:
    text_rect.center = (x,y)
  else:
    text_rect.x, text_rect.y = x, y
  surf.blit(text_surf, text_rect)

def render_hero_info(surface, info_obj):
  index = 0
  for key in info_obj:
    heading = f"{' '.join(key.split('_')).title()}:"
    if type(info_obj[key]) == list:
      info = ", ".join(info_obj[key]).title()
    elif type(info_obj[key]) == str:
      info = info_obj[key].title()
    else:
      info = info_obj[key]
    draw_text(surface, f"{heading} {info}", 25, x=20, y=520 + index * 25)
    index += 1

display_hero()