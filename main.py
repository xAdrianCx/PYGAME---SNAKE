
import pygame
from pygame import time
from settings import Game_Settings
from snake import Snake
from bait import Bait

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

    # Instantiate the bait.
    bait = Bait(gs, screen)

    # Main loop.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.key_pressed = pygame.K_UP
                if event.key == pygame.K_DOWN:
                    snake.key_pressed = pygame.K_DOWN
                if event.key == pygame.K_LEFT:
                    snake.key_pressed = pygame.K_LEFT
                if event.key == pygame.K_RIGHT:
                    snake.key_pressed = pygame.K_RIGHT
                    bait.update()
        screen.fill(gs.bg_color)

        bait.draw_bait()
        snake.update()
        snake.draw_snake()

        clock.tick(10)
        pygame.display.flip()


run_game()
