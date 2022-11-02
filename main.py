import pygame
from settings import Game_Settings


# Initialize pygame
pygame.init()

gs = Game_Settings()

# Create a screen.
screen = pygame.display.set_mode((gs.screen_width, gs.scrren_height))
caption = pygame.display.set_caption("Snake Game")
screen.fill(gs.bg_color)


while True:


