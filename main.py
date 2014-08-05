from game import Game
from consts import *

from pyo import Server
import pygame, random

screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
timer = pygame.time.Clock()

def main(): 
  pygame.init()
  server = Server().boot().start()

  games = []
  scales = [
      ([0, 311.13, 349.23, 392.0, 415.30, 466.16, 523.25, 587.33], 0.2)
      , ([0, 77.78, 87.31, 98.00, 103.83, 116.54, 130.81], 1)
      ]

  for scale,vol in scales:
    games.append(Game(scale, vol, randomize_colors()))

  main_loop(games)

def randomize_colors():
  random_color = (randomize_color_number(), randomize_color_number(), randomize_color_number())
  inverse_color = tuple(map(lambda x: MAX_COLOR - x, random_color))
  return random_color, inverse_color

def randomize_color_number():
  return random.randint(MIN_COLOR, MAX_COLOR)

def main_loop(games):
  keep_running = True
  ticks = 0

  while keep_running:
    timer.tick(fps)
    screen.fill(black)

    for e in pygame.event.get():
      if e.type is pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
        keep_running = False

    for i, game in enumerate(games):
      game.playSound(ticks)
      game.change_column_color(ticks)
      game.draw()
      screen.blit(game.surface, ((i%2)*game_screen_width,(i/2)*game_screen_height))
      pygame.draw.line(screen, white, (0, game_screen_height), (2*game_screen_width, game_screen_height))
      pygame.draw.line(screen, white, (game_screen_width, 0), (game_screen_width, 2*game_screen_height))

    pygame.display.flip()

    ticks += 1

    if ticks == fps*2:
      ticks = 0

      for game in games:
        game.new_generation()
        game.iterate()


if __name__ == '__main__':
  main()
