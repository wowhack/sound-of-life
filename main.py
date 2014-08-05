from game import Game
from consts import *

import pygame

screen = pygame.display.set_mode(screen_size)
timer = pygame.time.Clock()

def main(): 
  pygame.init()
  games = []
  for i in range(4):
    games.append(Game())
  main_loop(games)


def main_loop(games):
  while True:
    timer.tick(fps)

    screen.fill(black)
    
    for i, game in enumerate(games):
      game.iterate()
      screen.blit(game.surface, ((i%2)*game_screen_width,([0,0,1,1][i])*game_screen_height))

    pygame.draw.line(screen, white, (0, game_screen_height), (2*game_screen_width, game_screen_height))
    pygame.draw.line(screen, white, (game_screen_width, 0), (game_screen_width, 2*game_screen_height))

    pygame.display.flip()

if __name__ == '__main__':
  main()
