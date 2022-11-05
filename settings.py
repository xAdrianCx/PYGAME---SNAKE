import json

class Game_Settings():
    """A class that keeps game settings."""

    # Screen settings.
    screen_width = 1600
    scrren_height = 800
    bg_color = (0, 255, 0)

    # Snake settings.
    snake_length = 1
    snake_head = 20
    snake_body = []
    snake_color = (0, 0, 255)
    snake_speed = 20

    # Bait settings.
    bait_size = 20
    bait_color = (255, 0, 0)

    # Keep track of the score.
    score = 0
    high_score = 0


