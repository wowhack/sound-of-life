from pygame.locals import Rect

from consts import *

# some constants
MIN_COLOR = 0
MAX_COLOR = 255
COLOR_STEP = 85

class Cell:
  def __init__(self, x, y, alive=False):
    self.x = x
    self.y = y
    self.set_alive(alive)
    self.__reset_color()
    self.rect = Rect(x*cell_size, y*cell_size, cell_size, cell_size)

  def set_alive(self, alive=True):
    self.alive = alive
    self.age = 0

  def __reset_color(self):
    self.green = MAX_COLOR 
    self.red = MIN_COLOR

  # Returns the age if the cell dies, else -1
  def calculate_next(self, no_of_alive_neighbours):
    # these are the game of life rules
    if self.alive:
      if no_of_alive_neighbours < 2:
        # 'death by under-population'
        self.alive_next = False
        return self.age
      elif no_of_alive_neighbours == 2 or no_of_alive_neighbours == 3: 
        # 'enough neighbours to live on'
        self.alive_next = True
        self.__new_age()
      elif no_of_alive_neighbours > 3:
        # 'death by over-population'
        self.alive_next = False
        return self.age
    else:
      # if not alive
      if no_of_alive_neighbours == 3:
        # 'regenerate by reproduction'
        self.alive_next = True
        self.age = 0
        self.__new_age()
      else:
        # 'stay dead :('
        self.alive_next = False

    return -1

  def new_generation(self):
    self.alive = self.alive_next

  def __new_age(self):
    self.age += 1
    self.__calculate_color()

  def __calculate_color(self):
    if self.age == 1:
      self.__reset_color()
    else:
      if self.red != MAX_COLOR:
        self.red += COLOR_STEP 
      elif self.green == MIN_COLOR:
        pass
      elif self.red == MAX_COLOR:
        self.green -= COLOR_STEP

  def is_alive(self):
    return self.alive

  # the idea is that this will calculate a new color, based on the
  # cell's age
  def color(self):
    return (self.red, self.green, MIN_COLOR)
