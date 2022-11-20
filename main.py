import pygame
from pygame import time
from settings import GameSettings
from snake import Snake
from bait import Bait
import game_functions as gf
from game_stats import Scoreboard, PlayerNameBox


def run_game():
    """A function to run the game."""
    # Initialize pygame
    pygame.init()

    # Initialize the clock.
    clock = time.Clock()

    # Initialize Game_Settings.
    gs = GameSettings()

    # Create a screen.
    screen = pygame.display.set_mode((gs.screen_width, gs.screen_height))
    pygame.display.set_caption("Snake Game")
    screen.fill(gs.bg_color)

    # Initialize a player name box.
    pnb = PlayerNameBox(screen)

    # Initialize the scoreboard.
    sb = Scoreboard(gs, screen)

    # Instantiate the bait.
    bait = Bait(gs, screen, sb)

    # Instantiate the snake.
    snake = Snake(gs, screen)

    # Main loop.
    while True:

        if not gs.game_running and not gs.game_paused and not gs.game_over:
            gf.check_key_pressed(gs, screen, snake, pnb, sb)
            gf.ask_for_username(gs, screen, pnb)
        elif gs.game_running and not gs.game_paused and not gs.game_over:
            gf.play(gs, screen, sb, snake, bait, pnb, clock)
        elif gs.game_running and gs.game_paused:
            gf.check_key_pressed(gs, screen, snake, pnb, sb)
        elif gs.game_over:
            gf.game_over(gs, screen)
            gf.check_key_pressed(gs, screen, snake, pnb, sb)


run_game()
