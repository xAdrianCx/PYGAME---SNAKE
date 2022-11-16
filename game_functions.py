import pygame
import os
import json


def check_key_pressed(gs, screen, snake, pnb):
    """ Check which key was pressed."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.key_pressed = pygame.K_UP
            if event.key == pygame.K_DOWN:
                snake.key_pressed = pygame.K_DOWN
            if event.key == pygame.K_LEFT:
                snake.key_pressed = pygame.K_LEFT
            if event.key == pygame.K_RIGHT:
                snake.key_pressed = pygame.K_RIGHT
            if event.key == pygame.K_p:
                gs.game_paused = not gs.game_paused
                pause_msg_font = pygame.font.SysFont("Comic Sans", 50)
                pause_msg = "Game Paused..."
                pause_msg_img = pause_msg_font.render(pause_msg, True, "RED")
                screen.blit(pause_msg_img, ((gs.screen_width // 3), (gs.screen_height // 2)))
            if event.key == pygame.K_RETURN:
                pnb.player_name_list.append(pnb.player_name)
                pnb.player_name = ""
            if event.key == pygame.K_BACKSPACE:
                pnb.player_name = pnb.player_name[:-1]
            else:
                pnb.player_name += event.unicode


def check_snake_screen_collisions(gs, snake, sb):
    """ A function that detects snake-screen borders collisions."""
    if snake.rect.top < sb.rect_background.bottom:
        snake.reset()
        gs.snake_lives -= 1
    if snake.rect.bottom > snake.screen_rect.bottom:
        snake.reset()
        gs.snake_lives -= 1
    if snake.rect.right > snake.screen_rect.right:
        snake.reset()
        gs.snake_lives -= 1
    if snake.rect.left < snake.screen_rect.left:
        snake.reset()
        gs.snake_lives -= 1


def update_snake_length(gs, snake, bait, sb, pnb):
    """ A function that detects collisions.
    Updates the length of snake and creates a new bait at a random position."""
    if snake.rect.colliderect(bait.rect):
        gs.snake_length += 1
        # Increase the score.
        sb.score += 50
        if gs.snake_length > 10:
            sb.score += 100
        elif gs.snake_length > 20:
            sb.score += 200
        elif gs.snake_length > 30:
            sb.score += 300
        # Increase game speed.
        if gs.snake_length % 5 == 0:
            gs.game_speed += 1
        if sb.score > sb.highest_score:
            cwd = os.getcwd()
            os.chdir(cwd)
            with open("scoreboard.json", "r+") as file:
                data = json.load(file)
                best_player = {}
                if len(pnb.player_name_list) == 0:
                    name = "NoName"
                else:
                    name = pnb.player_name_list[0]
                high_score = sb.score
                best_player[name] = high_score
                data.update(best_player)
                file.seek(0)
                json.dump(data, file)
                sb.high_score_name = name
                sb.highest_score = high_score
        bait.update(sb)


def ask_for_username(gs, screen, pnb):
    """ Prompt for a username to be able to track the score."""
    screen.fill(gs.bg_color)
    pnb.draw_player_name_box()
    pygame.display.flip()
    if len(pnb.player_name_list) > 0:
        gs.game_running = True
