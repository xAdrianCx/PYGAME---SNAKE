
import pygame
from settings import Game_Settings
from snake import Snake


def run_game():
    """A function t run the game."""
    # Initialize pygame
    pygame.init()

    # Initialize Game_Settings.
    gs = Game_Settings()

    # Create a screen.
    screen = pygame.display.set_mode((gs.screen_width, gs.scrren_height))
    pygame.display.set_caption("Snake Game")
    screen.fill(gs.bg_color)

    # Instantiate the snake.
    snake = Snake(gs, screen)

    # Main loop.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    snake.up_arrow = True
        screen.fill(gs.bg_color)
        snake.draw_snake()
        pygame.display.flip()

run_game()
