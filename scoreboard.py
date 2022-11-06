import json
import pygame

class Scoreboard():
    """ A class to model a scoreboard."""
    def __init__(self, gs, screen):
        self.gs = gs
        self.screen = screen
        self.score = 0


