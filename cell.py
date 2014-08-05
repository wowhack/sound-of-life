from pygame.locals import Rect

from consts import *

class Cell:
  def __init__(self, x, y, colors, alive=False):
    self.x = x
    self.y = y
    self.set_alive(alive)
    self.default_color, self.inverse_color = colors
    self.color = self.default_color
    self.rect = Rect(x*cell_size, y*cell_size, cell_size, cell_size)

  def set_alive(self, alive=True):
    self.alive = alive
    self.alive_next = alive
    self.age = 0

  def switch_color(self):
    if self.color == self.default_color:
      self.color = self.inverse_color
    else:
      self.color = self.default_color

  def darken_color(self):
    self.color = tuple(map(lambda x: max(0, x - 51), self.color))
  
  # Returns the age if the cell dies, else -1
  def calculate_next(self, ns):
    if self.alive:
      if ns == 2 or ns == 3:
        self.alive_next = True
        self.age += 1
      else:
        self.alive_next = False
    else:
      if ns == 3:
        self.alive_next = True
        self.age = 0
      else:
        self.alive_next = False

    return self.age

  def new_generation(self):
    self.alive = self.alive_next

  def __new_age(self):
    self.age += 1

  def is_alive(self):
    return self.alive
