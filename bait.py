import pygame
import random


class Bait():
    """A class to model a bait."""
    def __init__(self, gs, screen):
        """Initialize class attributes."""
        self.gs = gs
        self. screen = screen
        self.screen_rect = self.screen.get_rect()
        # Create a rectangle.
        self.rect = pygame.Rect(0, 0, self.gs.bait_size, self.gs.bait_size)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Update the position of the bait."""
        self.x = random.randint(0, self.screen_rect.right - self.gs.bait_size)
        self.y = random.randint(0, self.screen_rect.right - self.gs.bait_size)
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_bait(self):
        """Draw the bait to the screen."""
        pygame.draw.rect(self.screen, self.gs.bait_color, self.rect)