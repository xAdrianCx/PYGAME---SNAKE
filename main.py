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

    # Instantiate the snake.
    snake = Snake(gs, screen)

    # Initialize a player name box.
    pnb = PlayerNameBox(screen)

    # Initialize the scoreboard.
    sb = Scoreboard(gs, screen)

    # Instantiate the bait.
    bait = Bait(gs, screen, sb)

    # Main loop.
    while True:
        if not gs.game_running and not gs.game_paused:
            gf.check_key_pressed(gs, screen, snake, pnb)
            gf.ask_for_username(gs, screen, pnb)
        if gs.game_running and not gs.game_paused:
            screen.fill(gs.bg_color)
            bait.draw_bait()
            snake.draw_snake()
            gf.check_key_pressed(gs, screen, snake, pnb)
            gf.check_snake_screen_collisions(gs, snake, sb)
            snake.update()
            gf.update_snake_length(gs, snake, bait, sb, pnb)
            sb.draw_stats(pnb)
            clock.tick(gs.game_speed)
            pygame.display.flip()
        if gs.game_running and gs.game_paused:
            gf.check_key_pressed(gs, screen, snake, pnb)


run_game()
