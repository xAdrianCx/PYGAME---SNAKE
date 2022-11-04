import pygame


class Snake():
    """A class that models a snake"""

    def __init__(self, gs, screen):
        """Initialize snake attributes"""
        self.gs = gs
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.gs.snake_head, sum(self.gs.snake_body))
        # Position the snake in the middle of the screen.
        self.rect.centerx = self.screen_rect.centerx + self.gs.snake_head // 2
        self.rect.centery = self.screen_rect.centery + self.gs.snake_head // 2
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Get the pressed key.
        self.key_pressed = None

    def update(self):
        """A method that updates the snake position."""
        if self.key_pressed == pygame.K_UP and self.y >= self.screen_rect.top + self.gs.snake_head:
            self.y -= self.gs.snake_speed
        if self.key_pressed == pygame.K_DOWN and self.y <= self.screen_rect.bottom - self.gs.snake_head * 2:
            self.y += self.gs.snake_speed
        if self.key_pressed == pygame.K_LEFT and self.x >= self.screen_rect.left + self.gs.snake_head:
            self.x -= self.gs.snake_speed
        if self.key_pressed == pygame.K_RIGHT and self.x <= self.screen_rect.right - self.gs.snake_head * 2:
            self.x += self.gs.snake_speed
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_snake(self):
        """Draws the snake on the screen"""
        pygame.draw.rect(self.screen, self.gs.snake_color, self.rect)