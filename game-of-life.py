#!/usr/bin/env

import sys, os, pygame, random
from pygame.locals import *

cell_size = 16
screen_size = width, height = 640, 480
game_size = game_width, game_height = width/cell_size, height/cell_size
screen = pygame.display.set_mode(screen_size)

cells = []

# colors
red = (255, 0, 0)
green = (0, 255, 0)

class Cell:
  def __init__(self, x, y, alive=False):
    self.x = x
    self.y = y
    self.set_alive(alive)
    self.rect = Rect(x*cell_size, y*cell_size, cell_size, cell_size)

  def set_alive(self, alive=True):
    self.alive = alive
    self.age = 0

  def calculate_next(self):
    no_of_alive_neighbours = self.__no_of_alive_neighbours()
    
    # these are the game of life rules
    if self.alive:
      if no_of_alive_neighbours < 2:
        # 'death by under-population'
        self.alive_next = False
      elif no_of_alive_neighbours == 2 or no_of_alive_neighbours == 3: 
        # 'enough neighbours to live on'
        self.alive_next = True
      elif no_of_alive_neighbours > 3:
        # 'death by over-population'
        self.alive_next = False
    else:
      # if not alive
      if no_of_alive_neighbours == 3:
        # 'regenerate by reproduction'
        self.alive_next = True
      else:
        # 'stay dead :('
        self.alive_next = False

  def new_generation(self):
    self.alive = self.alive_next

  def is_alive(self):
    return self.alive

  def __no_of_alive_neighbours(self):
    no_of_alive_neighbours = 0
    neighbours = self.__get_neighbours()
    for cell in neighbours:
      if cell.is_alive():
        no_of_alive_neighbours += 1
    return no_of_alive_neighbours
    
  def __get_neighbours(self):
    iter_start_x = self.x - 1
    iter_start_y = self.y - 1
    iter_end_x = self.x + 1
    iter_end_y = self.y + 1
 
    # corner cases
    if self.x == 0:
      iter_start_x = self.x
    if self.y == 0:
      iter_start_y = self.y
    if self.x == game_width-1:
      iter_end_x = self.x
    if self.y == game_height-1:
      iter_end_y = self.y
    
    neighbours = []
    for x in range(iter_start_x, iter_end_x+1):
      for y in range(iter_start_y, iter_end_y+1):
        if cells[y][x] == self:
          continue
        neighbours.append(cells[y][x])
    return neighbours

  def draw(self):
    if self.alive:
      color = self.__new_color()
      pygame.draw.rect(screen, color, self.rect)

  # the idea is that this will calculate a new color, based on the
  # cell's age
  def __new_color(self):
    return green

def init_randomized_cells():
  for y in range(game_height):
    row = []
    cells.append(row)
    for x in range(game_width):
      row.append(Cell(x, y, random.choice([True, False])))

def main_loop():
  while True:
    screen.fill((0,0,0))
    for x in range(game_width):
      for y in range(game_height):
        cell = cells[y][x]
        cell.draw()
        cell.calculate_next()
    for x in range(game_width):
      for y in range(game_height):
        cell = cells[y][x]
        cell.new_generation()
    pygame.display.flip()

def main(): 
  pygame.init()
  init_randomized_cells()
  main_loop()

# test method
# used for testing
def test():
  
  for y in range(game_height):
    cells.append(test_row(y))

  print "original"
  for y in range(game_width):
    for x in range(game_height):
      print cells[y][x].is_alive()

  for x in range(game_width):
    for y in range(game_height):
      cell = cells[y][x]
      cell.calculate_next()
  for x in range(game_width):
    for y in range(game_height):
      cell = cells[y][x]
      cell.new_generation()
  
  expected_result = [[False, False, False],
                     [True, True, True],
                     [False, False, False]]
  
  print "result"
  for y in range(game_width):
    for x in range(game_height):
      print cells[y][x].is_alive()

  print "expected"
  for y in range(game_width):
    for x in range(game_height):
      print expected_result[y][x]

  print "result == expected"
  for y in range(game_width):
    for x in range(game_height):
      print cells[y][x].is_alive() == expected_result[y][x]

def test_row(y):
  row = []
  row.append(Cell(0, y, False))
  row.append(Cell(1, y, True))
  row.append(Cell(2, y, False))
  return row

if __name__ == '__main__':
  main()
