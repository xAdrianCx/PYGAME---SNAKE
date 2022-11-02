import pygame


class Snake():
    """A class that models a snake"""

    # Initialize the snake.
    def __init_(self, screen, gs):
        """Initialize snake attributes"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.gs = gs
        self.rect = pygame.Rect(0, 0, self.gs.snake_head, self.gs.snake_head)
        self.rect.centerx = self.screen_rect.centerx

        self.rect.x = self.gs.screen_width
        self.rect.y = self.gs.snake_height

        # Store snake rect postion as a float number.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """A method that updates the snake position."""
        pass

    def draw_snake(self):
        """Draws the snake on the screen"""
        pygame.draw.rect(self.screen, self.gs.color, self.rect)