import pygame
from consts import *

class Banana():
  def __init__(self):
    self.images = [pygame.image.load("banana/bananas-%s.bmp" % x) for x in range(0, 8)]
    self.surface = pygame.Surface(screen_size)

  def draw(self, tick):
    self.surface.fill(black)

    image = self.images[tick % len(self.images)]
    x = image.get_width()
    y = image.get_height()
    
    self.surface.blit(image, (screen_width / 4 - x/2, screen_height / 4 - y/2))
