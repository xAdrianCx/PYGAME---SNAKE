import pygame


def check_key_pressed(gs, screen, snake, bait):
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


def update_snake_length(gs, snake, bait, sb):
    """ If collision, update the snake length."""
    if snake.rect.colliderect(bait.rect):
        gs.snake_length += 1
        # Increase the score.
        sb.score += 50
        # Increase game speed.
        if sb.score > 0 and sb.score % 500 == 0:
            gs.game_speed += 1
        bait.update()

def draw_screen(gs, screen, clock, snake, bait, sb):
    """ Draw eveything to screen."""
    screen.fill(gs.bg_color)
    sb.draw_score()
    bait.draw_bait()
    snake.draw_snake()
    snake.update()
    clock.tick(gs.game_speed)
    pygame.display.flip()






