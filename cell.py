from pygame.locals import Rect

from consts import *

class Cell:
  def __init__(self, x, y, alive=False):
    self.x = x
    self.y = y
    self.set_alive(alive)
    self.rect = Rect(x*cell_size, y*cell_size, cell_size, cell_size)

  def set_alive(self, alive=True):
    self.alive = alive
    self.age = 0

  def calculate_next(self, no_of_alive_neighbours):
    # these are the game of life rules
    if self.alive:
      if no_of_alive_neighbours < 2:
        # 'death by under-population'
        self.alive_next = False
      elif no_of_alive_neighbours == 2 or no_of_alive_neighbours == 3: 
        # 'enough neighbours to live on'
        self.alive_next = True
        self.__age()
      elif no_of_alive_neighbours > 3:
        # 'death by over-population'
        self.alive_next = False
    else:
      # if not alive
      if no_of_alive_neighbours == 3:
        # 'regenerate by reproduction'
        self.alive_next = True
        age = 0
        self.age()
      else:
        # 'stay dead :('
        self.alive_next = False

  def new_generation(self):
    self.alive = self.alive_next

  def is_alive(self):
    return self.alive

  # the idea is that this will calculate a new color, based on the
  # cell's age
  def color(self):
    return green
