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

def display_heroes():
  WIDTH, HEIGHT = 960, 720
  BACKGROUND_COLOUR = colours.BLUE
  FPS = 30
  
  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  clock = pygame.time.Clock()

  hero_data = load_hero_data()
  hero_images = [load_hero_image(hero['image']) for hero in hero_data]
  
  for hero in hero_data:
    print(type(hero))

  # GAME LOOP
  running = True

  while running:
    # Process Input (events)
    for event in pygame.event.get():
      if event.type == pygame.QUIT: # check for closing the window
        running = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        print(x,y)

    # Update
    # Draw / Render
    screen.fill(BACKGROUND_COLOUR)

    screen.blit(hero_images[0], (WIDTH // 4 - 150, 10))
    screen.blit(hero_images[1], (3 * WIDTH // 4 - 150, 10))

    draw_text(screen, hero_data[0]['name'].title(), 36, WIDTH // 4, 435, align_centre=True)
    draw_text(screen, hero_data[1]['name'].title(), 36, 3 * WIDTH // 4, 435, align_centre=True)
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

display_heroes()