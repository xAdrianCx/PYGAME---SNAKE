import pygame


class Snake():
    """A class that models a snake"""

    def __init__(self, gs, screen):
        """Initialize snake attributes"""
        self.gs = gs
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.gs.snake_head, self.gs.snake_head)
        # Position the snake in the middle of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.up_arrow = False
        self.down_arrow = False
        self.left_arrow = False
        self.right_arrow = False

    def update(self):
        """A method that updates the snake position."""
        if self.up_arrow and self.y >= self.screen_rect.top:
            self.y -= self.gs.snake_speed
        if self.down_arrow and self.y <= self.screen_rect.bottom:
            self.y += self.gs.snake_speed
        if self.left_arrow and self.x >= self.screen_rect.left:
            self.x -= self.gs.snake_speed
        if self.right_arrow and self.x <= self.screen_rect.right:
            self.x += self.gs.snake_speed

    def draw_snake(self):
        """Draws the snake on the screen"""
        pygame.draw.rect(self.screen, self.gs.snake_color, self.rect)