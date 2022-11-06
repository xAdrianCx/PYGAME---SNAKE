import pygame


def check_key_pressed(snake, pnb):
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
            if event.key == pygame.K_RETURN:
                pnb.player_name_list.append(pnb.player_name)
                pnb.player_name = ""
            if event.key == pygame.K_BACKSPACE:
                pnb.player_name = pnb.player_name[:-1]
            else:
                pnb.player_name += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pnb.player_name_box.collidepoint(event.pos):
                pnb.active = True


def update_snake_length(gs, snake, bait, sb):
    """ If collision, update the snake length."""
    if snake.rect.colliderect(bait.rect):
        gs.snake_length += 1
        # Increase the score.
        sb.score += 50
        # Increase game speed.
        if sb.score > 0 and sb.score % 500 == 0:
            gs.game_speed += 1
        bait.update(sb)

def draw_screen(gs, screen, clock, snake, bait, sb, pnb):
    """ Draw eveything to screen."""

    if len(pnb.player_name_list) <= 0:
        screen.fill(gs.bg_color)
        pnb.draw_player_name_box()
    else:
        screen.fill(gs.bg_color)
        sb.draw_score(pnb)
        bait.draw_bait()
        snake.draw_snake()
        snake.update(sb)
        clock.tick(gs.game_speed)
        pygame.display.flip()






