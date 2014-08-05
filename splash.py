import pygame, random
from pygame.locals import *

from cell import Cell
from consts import *


class Splash:
  def __init__(self, c):
    self.__init_randomized_cells()
    self.c = ((180, 73, 74), (75, 182, 181))
    self.surface = pygame.Surface(screen_size)

  def __init_randomized_cells(self):
    self.cells = []

    for y in range(game_height*2):
      row = []
      self.cells.append(row)

      for x in range(game_width*2):
        row.append(Cell(x, y, ((180, 180, 0), (75, 182, 181)), random.choice([True, False])))

  def draw(self):
    self.surface.fill(black)
    for cs in self.cells:
        for c in cs:
          if c.alive:
            pygame.draw.rect(self.surface, c.color, c.rect)

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
