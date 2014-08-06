#!/usr/bin/env

import pygame
from pygame.locals import *

from game import Game
from cell import Cell
from sound import Sound

class ChordsGame(Game):
  def playSound(self, ticks):
    if self.play_sound:
      for i, cell in enumerate(reversed(self.cellsT[ticks])):
        if cell.is_alive():
          self.sound.play(i)

  def change_column_color(self, ticks):
    for cell in self.cellsT[ticks]:
      cell.switch_color()
      if ticks != 0 and ticks != 8:
        cell.darken_color()

