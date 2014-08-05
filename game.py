#!/usr/bin/env

import sys, os, pygame, random
from pygame.locals import *

from cell import Cell

from consts import *

screen = pygame.display.set_mode(screen_size)
timer = pygame.time.Clock()

class Game:
  def __init__(self):
    self.__init_randomized_cells()
    self.surface = pygame.Surface(screen_size)

  def __init_randomized_cells(self):
    self.cells = []

    for y in range(game_height):
      row = []
      self.cells.append(row)

      for x in range(game_width):
        row.append(Cell(x, y, random.choice([True, False])))

  def iterate(self):
    self.surface.fill(black)

    for x in range(game_width):
      for y in range(game_height):
        cell = self.cells[y][x]

        if cell.alive:
          pygame.draw.rect(self.surface, cell.color(), cell.rect)

        cell.calculate_next(len(self.__alive_neighbours(cell)))

    for x in range(game_width):
      for y in range(game_height):
        cell = self.cells[y][x]
        cell.new_generation()

  def __neighbours(self, cell):
    iter_start_x = cell.x - 1
    iter_start_y = cell.y - 1
    iter_end_x = (cell.x + 1) % game_width
    iter_end_y = (cell.y + 1) % game_height
   
    neighbours = []
    for xi in range(iter_start_x, iter_end_x+1):
      for yi in range(iter_start_y, iter_end_y+1):
        if cell.x == xi and cell.y == yi:
          continue
        neighbours.append(self.cells[yi][xi])

    return neighbours

  def __alive_neighbours(self, cell):
    return filter(lambda c: c.is_alive(), self.__neighbours(cell))


def main_loop(games):
  while True:
    timer.tick(fps)

    screen.fill(black)
    
    for i in range(4):
      games[i].iterate()
      screen.blit(games[i].surface, ((i%2)*game_screen_width,([0,0,1,1][i])*game_screen_height))

    pygame.draw.line(screen, white, (0, game_screen_height), (2*game_screen_width, game_screen_height))
    pygame.draw.line(screen, white, (game_screen_width, 0), (game_screen_width, 2*game_screen_height))

    pygame.display.flip()

def main(): 
  pygame.init()
  games = []
  for i in range(4):
    games.append(Game())
  main_loop(games)

if __name__ == '__main__':
  main()
