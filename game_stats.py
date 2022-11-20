import json
import pygame
import os


class PlayerNameBox:
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
        self.player_name_box = pygame.Rect((self.screen_rect.right // 3),
                                           (self.screen_rect.bottom // 3),
                                           self.width // 2, self.height)
        # Set an active color for the box(after player clicks into the box).
        self.color = pygame.Color(204, 102, 0)

        # Create a text on top of the player_name_box.
        self.text = pygame.font.SysFont("Comic Sans", 15)

    def draw_player_name_box(self):
        """ Draw the player name box to the screen."""
        pygame.draw.rect(self.screen, self.color, self.player_name_box)
        text_surface = self.name_box_font.render(self.player_name, True, (255, 255, 255))
        text_on_top = self.text.render("Type your name and press 'Enter' to start the game", True, (255, 255, 255))
        self.screen.blit(text_on_top, (self.player_name_box.x + 5, self.player_name_box.y - 30))
        self.screen.blit(text_surface, (self.player_name_box.x + 5, self.player_name_box.y + 0))
        self.player_name_box.w = max(400, text_surface.get_width() + 10)
        pygame.display.flip()


class Scoreboard:
    """ A class to model a scoreboard."""
    def __init__(self, gs, screen):
        self.gs = gs
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.score = 0
        self.score_color = (179, 171, 171)
        self.rect_background = pygame.Rect(0, 0, self.screen_rect.right, 40)
        self.rect_background.top = self.screen_rect.top
        cwd = os.getcwd()
        os.chdir(cwd)
        # Get the highest score from the database.
        with open("scoreboard.json", "r+") as data_file:
            data = json.load(data_file)
        self.high_score_name = max(data, key=data.get)
        self.highest_score = max(data.values())

    def draw_stats(self, pnb):
        """ Draw the score to the screen.
        Also draws the lives left."""
        # Create a high score font object.
        high_score_msg_font = pygame.font.SysFont("Comic Sans", 25)
        high_score_msg = f"All Time Highest Score --> {self.high_score_name}: {self.highest_score}"
        high_score_img = high_score_msg_font.render(high_score_msg, True, "BLUE")
        # Create a score font object.
        score_msg_font = pygame.font.SysFont("Comic Sans", 25)
        if len(pnb.player_name_list) == 0 or pnb.player_name_list[0] == "":
            pnb.player_name_list[0] = "NoName"
            score_msg = f"{pnb.player_name_list[0]}'s Score: {self.score}"
        else:
            score_msg = f"{pnb.player_name_list[0]}'s Score: {self.score}"
        score_img = score_msg_font.render(score_msg, True, "BLUE")
        # Create the lives.
        snake_lives = pygame.Rect(0, 10, self.gs.snake_head, self.gs.snake_head)
        snake_lives_color = self.gs.snake_color
        snake_lives.right = self.screen_rect.right - 110
        snake_lives_list = []
        x = self.screen_rect.right - 110
        y = 10
        for i in range(self.gs.snake_lives):
            snake_lives_list.append(pygame.Rect(x, y, self.gs.snake_head, self.gs.snake_head))
            x += 30
        # Draw everything to the screen.
        pygame.draw.rect(self.screen, self.score_color, self.rect_background)
        [pygame.draw.rect(self.screen, snake_lives_color, life) for life in snake_lives_list]
        self.screen.blit(score_img, (10, 5))
        self.screen.blit(high_score_img, ((self.screen_rect.right // 2) - 200, 5))

    def reset_stats(self):
        """ Reset all stats."""
        if self.gs.game_over:
            self.score = 0
            self.gs.snake_lives = 3
            self.gs.snake_body = []
            self.gs.snake_length = 1
            self.gs.game_speed = 20
