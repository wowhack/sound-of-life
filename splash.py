import pygame, random
from pygame.locals import *

from cell import Cell
from consts import *

class Splash:
  def __init__(self):
    self.time_count = 0
    self.__init_randomized_cells()
    self.surface = pygame.Surface(screen_size)

    # stuff related to the logo
    self.logo_surface = pygame.Surface(screen_size)
    self.logo = pygame.image.load("logo.bmp")
    self.logo_alpha = 0

  def __init_randomized_cells(self):
    self.cells = []

    for y in range(game_height*2 - 1):
      row = []
      self.cells.append(row)

      for x in range(game_width*2 - 1):
        row.append(Cell(x, y, ((180, 180, 0), (75, 182, 181)), random.choice([True, False])))

  def draw(self, delta):
    self.time_count += delta

    self.surface.fill(black)
    if self.logo_alpha < 255:
      for cs in self.cells:
        for c in cs:
          if c.alive:
            pygame.draw.rect(self.surface, c.color, c.rect)
    if self.time_count >= time_til_logo:
      self.logo_surface.fill(black)
      self.logo_surface.blit(self.logo, ((screen_width/2) - (self.logo.get_width() / 2), (screen_height/2) - (self.logo.get_height() / 2)))
      self.logo_surface.set_alpha(self.logo_alpha)
      self.surface.blit(self.logo_surface, (0,0))
      if self.logo_alpha < 255:
        self.logo_alpha += 5

  def iterate(self):
    for cs in self.cells: 
      for c in cs:
        c.calculate_next(len(self.__alive_neighbours(c)))

  def new_generation(self):
    for cs in self.cells:
      for cell in cs:
        cell.new_generation()

  def __neighbours(self, cell):
    iter_start_x = cell.x - 1
    iter_start_y = cell.y - 1
    iter_end_x = cell.x + 1
    iter_end_y = cell.y + 1
   
    neighbours = []
    for xi in range(iter_start_x, iter_end_x+1):
      for yi in range(iter_start_y, iter_end_y+1):
        if cell.x == xi and cell.y == yi:
          continue
        neighbours.append(self.cells[yi % game_height][xi % game_width])

    return neighbours

  def __alive_neighbours(self, cell):
    return filter(lambda c: c.is_alive(), self.__neighbours(cell))
