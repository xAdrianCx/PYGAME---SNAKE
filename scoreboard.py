import json
import pygame

class Scoreboard():
    """ A class to model a scoreboard."""
    def __init__(self, gs, screen):
        self.gs = gs
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.score = 0
        self.score_color = (179, 171, 171)
        self.rect_background = pygame.Rect(0, 0, self.screen_rect.right, 40)

    def draw_score(self):
        font = pygame.font.SysFont(None, 35)
        score_msg = f"Your Score: {self.score}"
        score_img = font.render(score_msg, True, "BLUE")
        pygame.draw.rect(self.screen, self.score_color, self.rect_background)
        self.screen.blit(score_img, (20, 10))

