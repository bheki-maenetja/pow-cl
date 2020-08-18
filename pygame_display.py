# Standard Library Imports
from sys import argv
from json import loads
# Third-Party imports
import pygame

# Local Imports

# Display hero - display the hero's picture along with all their info
def display_hero():
  WIDTH, HEIGHT = 540, 720
  BLUE = (0, 0, 255)
  FPS = 30

  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  clock = pygame.time.Clock()

  # GAME LOOP
  running = True

  while running:
    # Process Input (events)
    for event in pygame.event.get():
      if event.type == pygame.QUIT: # check for closing the window
        running = False
        pygame.quit()

    # Update
    # Draw / Render
    screen.fill(BLUE)

    # AFTER Drawing Everything, Flip the Display
    pygame.display.flip()

    # Keep Game Loop Running at Given FPS
    clock.tick(FPS)

# Load hero info - loads hero information from the current_hero file
def load_hero_info():
  try:
    file_handler = open(argv[1], 'r')
    data = next(line for line in file_handler.readlines())
    hero_data = loads(data)
    print(type(hero_data), hero_data)
  except:
    print('Could not load hero info')

load_hero_info()
display_hero()