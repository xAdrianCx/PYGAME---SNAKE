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
                # To be continued
                while True:
                    screen.fill((255, 0, 0))
                    pygame.display.flip()

            if event.key == pygame.K_RETURN:
                pnb.player_name_list.append(pnb.player_name)
                pnb.player_name = ""
            if event.key == pygame.K_BACKSPACE:
                pnb.player_name = pnb.player_name[:-1]
            else:
                pnb.player_name += event.unicode


def check_snake_screen_collisions(snake, sb):
    if snake.rect.top < sb.rect_background.bottom:
        return True
    if snake.rect.bottom > snake.screen_rect.bottom:
        return True
    elif snake.rect.right > snake.screen_rect.right:
        return True
    elif snake.rect.left < snake.screen_rect.left:
        return True


def update_snake_length(gs, snake, bait, sb, pnb):
    """ If collision, update the snake length."""
    if snake.rect.colliderect(bait.rect):
        gs.snake_length += 1
        # Increase the score.
        sb.score += 50
        # Increase game speed.
        if sb.score > 0 and sb.score % 500 == 0:
            gs.game_speed += 1
        if sb.score > sb.highest_score:
            cwd = os.getcwd()
            os.chdir(cwd)
            with open("scoreboard.json", "r+") as file:
                data = json.load(file)
                best_player = {}
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
        gs.game_active = False


def draw_screen(gs, screen, clock, snake, bait, sb, pnb):
    """ Draw everything to screen."""
    screen.fill(gs.bg_color)
    sb.draw_score(pnb)
    bait.draw_bait()
    snake.draw_snake()
    snake.update(sb)
    clock.tick(gs.game_speed)
    pygame.display.flip()
