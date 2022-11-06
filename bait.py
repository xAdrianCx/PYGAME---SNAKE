import pygame
import random


class Bait():
    """A class to model a bait."""
    def __init__(self, gs, screen, sb):
        """Initialize class attributes."""
        self.gs = gs
        self. screen = screen
        self.screen_rect = self.screen.get_rect()
        # Create a rectangle.
        self.rect = pygame.Rect(0, 0, self.gs.bait_size, self.gs.bait_size)
        self.update(sb)

    def update(self, sb):
        """Update the position of the bait."""
        self.rect.x = random.randint(0, (self.screen_rect.right - self.gs.bait_size) / self.gs.bait_size) * self.gs.bait_size
        self.rect.y = random.randint(sb.rect_background.bottom, (self.screen_rect.bottom - self.gs.bait_size) / self.gs.bait_size) * self.gs.bait_size

    def draw_bait(self):
        """Draw the bait to the screen."""
        pygame.draw.rect(self.screen, self.gs.bait_color, self.rect)