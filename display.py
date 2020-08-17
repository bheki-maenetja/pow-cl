# Standard Library Imports
# Third Party Imports
from tabulate import tabulate
import pygame
# Local Imports

# Get Search Table -- returns tabulated search data
def get_search_table(search_data):
  if len(search_data) == 0:
    print("No Matches. Try again!")
    return
  formatted_data = [{ key.upper(): obj[key] for key in obj if key != 'id' } for obj in search_data]
  tabulated_data = tabulate(formatted_data, headers="keys", showindex=range(1, len(formatted_data) + 1))
  print(tabulated_data, end="\n\n")

# Display superhero information in a new pygame window
def set_up_window():
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

    # Update
    
    # Draw / Render
    screen.fill(BLUE)

    # AFTER Drawing Everything, Flip the Display
    pygame.display.flip()

    # Keep Game Loop Running at Given FPS
    clock.tick(FPS)