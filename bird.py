import pygame
import random

def draw_bird(x, y):
    screen.blit(bird_image, (x, y))

def draw_pipes(pipe_list):
    for pipe in pipe_list:
        screen.blit(pipe_image, pipe)

def draw_text(text, x, y, font_size=24, color=(255, 255, 255)):
    font = pygame.font.Font(None, font_size)  # Use default system font
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def check_collision(pipe_list, bird_rect):
    for pipe in pipe_list:
        if bird_rect.colliderect(pipe):
            return True
    if bird_rect.top <= 0 or bird_rect.bottom >= SCREEN_HEIGHT:
        return True
    return False

def create_pipe():
    random_height = random.randint(200, 400)
    bottom_pipe = pipe_image.get_rect(midtop=(SCREEN_WIDTH + 50, random_height))
    top_pipe = pipe_image.get_rect(midbottom=(SCREEN_WIDTH + 50, random_height - pipe_gap))
    return bottom_pipe, top_pipe

def main():
    pygame.init()

    global SCREEN_WIDTH, SCREEN_HEIGHT, screen, bird_image, pipe_image, background_image, clock, pipe_gap
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Flappy Bird')

    bird_image = pygame.image.load('bird.png')
    pipe_image = pygame.image.load('pipe.png')
    background_image = pygame.image.load('background.png')
    clock = pygame.time.Clock()

    bird_x = 50
    bird_y = 300
    bird_y_change = 0
    gravity = 0.5
    pipe_width = 70
    pipe_height = 400
    pipe_gap = 200
    pipe_x_change = -4
    score = 0

    pipes = []
    pipes.extend(create_pipe())

    # Display your name on the background with dark color
    your_name = "Gopi Ravada"
    name_x = 20
    name_y = 20
    name_color = (0, 0, 0)  # Dark color (black)

    running = True
    while running:
        game_over = False  # Reset game_over flag for each game loop iteration

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_y_change = -8
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    bird_y_change = 0

        bird_y_change += gravity
        bird_y += bird_y_change

        for i in range(len(pipes)):
            pipes[i] = pipes[i].move(pipe_x_change, 0)
        
        if pipes[0].right <= 0:
            pipes.pop(0)
            pipes.pop(0)
            pipes.extend(create_pipe())

        screen.blit(background_image, (0, 0))
        draw_text(your_name, name_x, name_y, color=name_color)  # Display your name with dark color
        draw_bird(bird_x, bird_y)
        draw_pipes(pipes)

        bird_rect = bird_image.get_rect(center=(bird_x, bird_y))

        if check_collision(pipes, bird_rect):
            game_over = True

        pygame.display.update()
        clock.tick(30)

        if game_over:
            break  # Exit the game loop immediately upon collision or out of bounds

    while game_over:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        text = font.render('Game Over', True, (255, 0, 0))
        screen.blit(text, (50, 300))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_over = False
                    main()

    pygame.quit()

if __name__ == "__main__":
    main()
