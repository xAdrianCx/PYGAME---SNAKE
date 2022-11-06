import json
import pygame
import os

class Player_Name_Box():
    """ Store the game stats."""
    def __init__(self, screen):
        """ Initialize the stats."""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # Create a font object for storing the name of the player.
        self.name_box_font = pygame.font.SysFont("Comic Sans", 25)
        self.player_name_list = []
        self.player_name = ""
        self.width = 200
        self.height = 40
        # Create a box for users to provide their name.
        self.player_name_box = pygame.Rect(self.screen_rect.right // 2, self.screen_rect.bottom // 2, self.width, self.height)
        # Set an active color for the box(after player clicks into the box).
        self.active_color = pygame.Color(153, 255, 255)
        # Set a passive color of the box.
        self.passive_color = pygame.Color(102, 0, 0)
        # Set an active flag.
        self.active = False
        self.color = None
        if self.active == True:
            self.color = self.active_color
        else:
            self.color = self.passive_color

    def draw_player_name_box(self):
        """ Draw the player name box to the screen."""
        pygame.draw.rect(self.screen, self.color, self.player_name_box)
        text_surface = self.name_box_font.render(self.player_name, True, (255, 255, 255))
        self.screen.blit(text_surface, (self.player_name_box.x + 5, self.player_name_box.y + 5))
        self.player_name_box.w = max(100, text_surface.get_width() + 10)
        pygame.display.flip()


class Scoreboard():
    """ A class to model a scoreboard."""
    def __init__(self, gs, screen):
        self.gs = gs
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.score = 0
        self.score_color = (179, 171, 171)
        self.rect_background = pygame.Rect(0, 0, self.screen_rect.right, 40)
        self.rect_background.top = self.screen_rect.top

    def draw_score(self, pnb):
        cwd = os.getcwd()
        os.chdir(cwd)
        with open("scoreboard.json", "r+") as data_file:
            data = json.load(data_file)
        highscore_name = max(data, key=data.get)
        highest_score = max(data.values())
        # Create a highscore font object.
        highscore_msg_font = pygame.font.SysFont("Comic Sans", 25)
        highscore_msg = f"All Time Highest Score --> {highscore_name.title()}: {highest_score}"
        highscore_img = highscore_msg_font.render(highscore_msg, True, "BLUE")
        # Create a score font object.
        score_msg_font = pygame.font.SysFont("Comic Sans", 25)
        score_msg = f"{pnb.player_name_list[0]}'s Score: {self.score}"
        score_img = score_msg_font.render(score_msg, True, "BLUE")
        # Draw everything to the screen.
        pygame.draw.rect(self.screen, self.score_color, self.rect_background)
        self.screen.blit(score_img, (10, 5))
        self.screen.blit(highscore_img, ((self.screen_rect.right // 2) - 200, 5))

