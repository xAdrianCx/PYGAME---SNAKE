import pygame


class Snake():
    """A class that models a snake"""

    def __init__(self, gs, screen):
        """Initialize snake attributes"""
        self.gs = gs
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Create a rectangle.
        self.rect = pygame.Rect(0, 0, self.gs.snake_head, self.gs.snake_head)
        # Position the snake in the middle of the screen.
        self.rect.center = (self.screen_rect.centerx - (self.gs.snake_head / 2), self.screen_rect.centery)


        # Get the pressed key.
        self.key_pressed = None

    def update(self, sb):
        """A method that updates the snake position."""
        if self.key_pressed == pygame.K_UP and self.rect.top >= self.screen_rect.top + sb.rect_background.bottom + self.gs.snake_head:
            self.rect.top -= self.gs.snake_speed
        if self.key_pressed == pygame.K_DOWN and self.rect.bottom <= self.screen_rect.bottom - self.gs.snake_head:
            self.rect.bottom += self.gs.snake_speed
        if self.key_pressed == pygame.K_LEFT and self.rect.left >= self.screen_rect.left + self.gs.snake_head:
            self.rect.left -= self.gs.snake_speed
        if self.key_pressed == pygame.K_RIGHT and self.rect.right <= self.screen_rect.right - self.gs.snake_head:
            self.rect.right += self.gs.snake_speed

        self.gs.snake_body.append(self.rect.copy())
        self.gs.snake_body = self.gs.snake_body[-self.gs.snake_length:]

    def draw_snake(self):
        """Draws the snake on the screen"""
        [pygame.draw.rect(self.screen, self.gs.snake_color, block) for block in self.gs.snake_body]