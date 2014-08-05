#!/usr/bin/env

import sys, os, pygame, random
from pygame.locals import *

from cell import Cell

from consts import *

screen = pygame.display.set_mode(screen_size)
timer = pygame.time.Clock()
fps = 5

cells = []

def neighbours(cell, cells):
  iter_start_x = cell.x - 1
  iter_start_y = cell.y - 1
  iter_end_x = cell.x + 1
  iter_end_y = cell.y + 1
 
  # corner cases
  if cell.x == 0:
    iter_start_x = cell.x
  if cell.y == 0:
    iter_start_y = cell.y
  if cell.x == game_width-1:
    iter_end_x = cell.x
  if cell.y == game_height-1:
    iter_end_y = cell.y
  
  neighbours = []
  for xi in range(iter_start_x, iter_end_x+1):
    for yi in range(iter_start_y, iter_end_y+1):
      if cell.x == xi and cell.y == yi:
        continue
      neighbours.append(cells[yi][xi])

  return neighbours

def alive_neighbours(cell, cells):
  return filter(lambda c: c.is_alive(), neighbours(cell, cells))


def init_randomized_cells():
  for y in range(game_height):

    row = []
    cells.append(row)

    for x in range(game_width):
      row.append(Cell(x, y, random.choice([True, False])))

def main_loop():
  while True:
    timer.tick(fps)

    screen.fill(black)

    for x in range(game_width):
      for y in range(game_height):
        cell = cells[y][x]

        if cell.alive:
          pygame.draw.rect(screen, cell.color(), cell.rect)

        cell_age = cell.calculate_next(len(alive_neighbours(cell, cells)))
        if cell_age != -1:
          # play a note
          print cell_age

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
