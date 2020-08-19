# Standard Library Imports
from sys import argv
from json import loads
import io
from urllib.request import urlopen
# Third-Party imports
import pygame

# Local Imports

# Display hero - display the hero's picture along with all their info
def display_hero():
  WIDTH, HEIGHT = 540, 720
  BLUE = (0, 0, 255)
  FPS = 30
  
  hero_data = load_hero_data()
  image_url = hero_data['image']
  image_str = urlopen(image_url).read()
  image_file = io.BytesIO(image_str)
  hero_image = pygame.image.load(image_file)

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

    # Update
    # Draw / Render
    screen.fill(BLUE)
    screen.blit(hero_image, (0,0))
    # AFTER Drawing Everything, Flip the Display
    pygame.display.flip()

    # Keep Game Loop Running at Given FPS
    clock.tick(FPS)

# Load hero info - loads hero information from the current_hero file
def load_hero_data():
  try:
    file_handler = open(argv[1], 'r')
    data = next(line for line in file_handler.readlines())
    hero_data = loads(data)
    return hero_data
  except:
    print('Could not load hero info')

display_hero()