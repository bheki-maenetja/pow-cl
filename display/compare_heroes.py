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
  WIDTH, HEIGHT = 540, 720
  BACKGROUND_COLOUR = colours.BLUE
  FPS = 30
  
  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  clock = pygame.time.Clock()

  hero_data = load_hero_data()
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
    # AFTER Drawing Everything, Flip the Display
    pygame.display.flip()

    # Keep Game Loop Running at Given FPS
    clock.tick(FPS)

# Load hero info - loads hero information from the current_hero file
def load_hero_data():
  try:
    file_handler = open(path.join(path.dirname(__file__), argv[1]), 'r')
    data = [loads(line) for line in file_handler.readlines()]
    # hero_data = loads(data)
    return data
  except:
    print('Could not load hero info')

display_heroes()