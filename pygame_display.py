# Standard Library Imports
from sys import argv
from json import loads
import io
from urllib.request import urlopen
# Third-Party imports
import pygame

# Local Imports
import colours

# Button Sprites - spirites that represent buttons on a screen
class Button(pygame.sprite.Sprite):
  def __init__(self, x, y, text):
    super(Button, self).__init__()
    self.image = pygame.Surface((200, 50))
    self.image.fill(colours.RED)
    draw_text(self.image, text, 30, 100, 25)
    self.rect = self.image.get_rect(center=(x, y))
  
  def get_rect(self):
    return self.rect

# Display hero - display the hero's picture along with all their info
def display_hero():
  WIDTH, HEIGHT = 540, 720
  BACKGROUND_COLOUR = colours.WHITE
  FPS = 30
  
  hero_data = load_hero_data()
  hero_image = load_hero_image(hero_data['image'])
  
  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  clock = pygame.time.Clock()
  new_button = Button(WIDTH // 2, HEIGHT - 100, 'Biography')
  buttons = pygame.sprite.Group()
  buttons.add(new_button)

  # GAME LOOP
  running = True

  while running:
    # Process Input (events)
    for event in pygame.event.get():
      if event.type == pygame.QUIT: # check for closing the window
        running = False

    # Update
    # Draw / Render
    screen.fill(BACKGROUND_COLOUR)
    screen.blit(hero_image, (WIDTH // 2 - 150, 10))
    draw_text(screen, hero_data['name'].title(), 36, WIDTH // 2, 435)
    buttons.draw(screen)
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

def load_hero_image(image_url):
  image_str = urlopen(image_url).read()
  image_file = io.BytesIO(image_str)
  hero_image = pygame.image.load(image_file)
  return pygame.transform.scale(hero_image, (300,400))

# Text handling - writes text on the pygame window
def draw_text(surf, text, font_size, x, y, font_name='arial'):
  chosen_font = pygame.font.match_font(font_name)
  font = pygame.font.Font(chosen_font, font_size)
  text_surf = font.render(text, True, colours.BLACK)
  text_rect = text_surf.get_rect()
  text_rect.center = (x,y)
  surf.blit(text_surf, text_rect)

display_hero()