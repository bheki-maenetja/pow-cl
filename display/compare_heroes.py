# Standard Library Imports
from sys import argv
from os import path
from json import loads
import io
from urllib.request import urlopen

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
      self.image.fill(colours.BLUE)
      draw_text(self.image, text, font_size, width // 2, height // 2, font_colour=colours.WHITE, align_centre=True)
    else:
      self.image.fill(colours.RED)
      draw_text(self.image, text, font_size, width // 2, height // 2, align_centre=True)
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
    self.image.fill(colours.BLUE)
    draw_text(self.image, self.text, self.font_size, self.width // 2, self.height // 2, font_colour=colours.WHITE, align_centre=True)
  
  def de_select_button(self):
    self.is_selected = False
    self.image.fill(colours.RED)
    draw_text(self.image, self.text, self.font_size, self.width // 2, self.height // 2, font_colour=colours.BLACK, align_centre=True)

# Display heroes - display the heroes' pictures along with all their info
def display_heroes():
  WIDTH, HEIGHT = 960, 720
  BACKGROUND_COLOUR = colours.WHITE
  FPS = 30
  
  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  clock = pygame.time.Clock()

  hero_data = load_hero_data()
  hero_images = [load_hero_image(hero['image']) for hero in hero_data]
  
  buttons = pygame.sprite.Group()
  powerstats_button = Button(WIDTH // 2, HEIGHT // 2 - 30, 100, 50, "Powerstats", 20, is_selected=True)
  bio_button = Button(WIDTH // 2, HEIGHT // 2 + 30, 100, 50, "Bio", 20)
  buttons.add(powerstats_button)
  buttons.add(bio_button)

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
            for b in buttons: 
              b.de_select_button()
            button.select_button()

    # Update
    # Draw / Render
    screen.fill(BACKGROUND_COLOUR)

    screen.blit(hero_images[0], (WIDTH // 4 - 150, 10))
    screen.blit(hero_images[1], (3 * WIDTH // 4 - 150, 10))

    draw_text(screen, hero_data[0]['name'].title(), 36, WIDTH // 4, 435, align_centre=True)
    draw_text(screen, hero_data[1]['name'].title(), 36, 3 * WIDTH // 4, 435, align_centre=True)
    
    buttons.draw(screen)
    selected_button = next(button for button in buttons if button.is_button_selected())

    if selected_button.get_text().lower() == 'powerstats':
      render_hero_info(screen, hero_data[0]['powerstats'], margin=WIDTH // 4 - 150)
      render_hero_info(screen, hero_data[1]['powerstats'], margin=3 * WIDTH // 4 - 150)
    elif selected_button.get_text().lower() == 'bio':
      render_hero_info(screen, hero_data[0]['appearance'], margin=WIDTH // 4 - 150)
      render_hero_info(screen, hero_data[1]['appearance'], margin=3 * WIDTH // 4 - 150)

    # AFTER Drawing Everything, Flip the Display
    pygame.display.flip()

    # Keep Game Loop Running at Given FPS
    clock.tick(FPS)

# Load hero info - loads hero information from the current_hero file
def load_hero_data():
  try:
    file_handler = open(path.join(path.dirname(__file__), argv[1]), 'r')
    data = [loads(line) for line in file_handler.readlines()]
    return data
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

def render_hero_info(surface, info_obj, margin):
  index = 0
  for key in info_obj:
    heading = f"{' '.join(key.split('_')).title()}:"
    if type(info_obj[key]) == list:
      info = ", ".join(info_obj[key]).title()
    elif type(info_obj[key]) == str:
      info = info_obj[key].title()
    else:
      info = info_obj[key]
    draw_text(surface, f"{heading} {info}", 25, x=margin, y=485 + index * 25)
    index += 1

display_heroes()