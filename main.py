import pygame
from pygame import time
from settings import Game_Settings
from snake import Snake
from bait import Bait
import game_functions as gf
from game_stats import Scoreboard, Player_Name_Box


def run_game():
    """A function to run the game."""
    # Initialize pygame
    pygame.init()

    # Initialize the clock.
    clock = time.Clock()

    # Initialize Game_Settings.
    gs = Game_Settings()

    # Create a screen.
    screen = pygame.display.set_mode((gs.screen_width, gs.scrren_height))
    pygame.display.set_caption("Snake Game")
    screen.fill(gs.bg_color)

    # Instantiate the snake.
    snake = Snake(gs, screen)

    # Initialize the scoreboard.
    sb = Scoreboard(gs, screen)

    # Instantiate the bait.
    bait = Bait(gs, screen, sb)

    # Initialize a player name box.
    pnb = Player_Name_Box(screen)

    # Main loop.
    while True:
        gf.check_key_pressed(snake, pnb)
        gf.draw_screen(gs, screen, clock, snake, bait, sb, pnb)
        gf.update_snake_length(gs, snake, bait, sb)


run_game()
