import pygame

MELODY = 0
CHORDS = 1 

# some constants
MIN_COLOR = 0
MAX_COLOR = 255
COLOR_STEP = 85

# in pixels
#cell_size = 40

# cells
game_size = game_width, game_height = 16, 9 

pygame.display.init()
max_resolution = pygame.display.list_modes()[0]

screen_size = screen_width, screen_height = max_resolution

game_screen_size = game_screen_width, game_screen_height = screen_width / 2, screen_height / 2

cell_size = game_screen_width / game_size[0]

# in pixels
#game_screen_size = game_screen_width, game_screen_height = game_width * cell_size, game_height * cell_size

# in pixels
# 2, because we want 4 games on one screen
#screen_size = width, height = 2 * game_screen_width, 2 * game_screen_height

# colors
black = (0, 0, 0)
white = (255, 255, 255)

fps = 8
beat_duration = 0.5
