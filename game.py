#!/usr/bin/env

import pygame, random
from pygame.locals import *

from cell import Cell
from consts import *
from sound import Sound

class Game:
  def __init__(self, scale, vol, colors):
    self.colors = colors
    self.__init_randomized_cells()
    self.surface = pygame.Surface(screen_size)
    self.sound = Sound(scale, vol)

  def __init_randomized_cells(self):
    self.cells = []

    for y in range(game_height):
      row = []
      self.cells.append(row)

      for x in range(game_width):
        row.append(Cell(x, y, self.colors, random.choice([True, False])))

      self.cellsT = [list(i) for i in zip(*self.cells)]

  def playSound(self, ticks):
    self.sound.play(len(filter(lambda c: c.alive, self.cellsT[ticks])))
    for i, cell in enumerate(reversed(self.cellsT[ticks])):
      if cell.is_alive():
        self.sound.play(i)

  def change_column_color(self, ticks):
    for cell in self.cellsT[ticks]:
      cell.switch_color()

  def draw(self):
    self.surface.fill(black)
    for x in range(game_width):
      for y in range(game_height):
        cell = self.cells[y][x]
        if cell.alive:
          pygame.draw.rect(self.surface, cell.color, cell.rect)

  def iterate(self):
    for x in range(game_width):
      for y in range(game_height):
        cell = self.cells[y][x]
        cell.calculate_next(len(self.__alive_neighbours(cell)))

  def new_generation(self):
    for x in range(game_width):
      for y in range(game_height):
        cell = self.cells[y][x]
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
