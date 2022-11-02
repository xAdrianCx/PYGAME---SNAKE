import pygame


class Snake():
    """A class that models a snake"""

    def __init_(self, gs, screen):
        """Initialize snake attributes"""
        self.gs = gs
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.gs.snake_head, self.gs.snake_head)
        # Position the snake in the middle of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery


    def update(self):
        """A method that updates the snake position."""
        pass

    def draw_snake(self):
        """Draws the snake on the screen"""
        pygame.draw.rect(self.screen, self.gs.color, self.rect)