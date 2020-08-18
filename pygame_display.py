# Standard Library Imports
from sys import argv
# Third-Party imports
import pygame

# Local Imports

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

display_hero()