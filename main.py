import pygame


# CONSTANTS
WIDTH = 1280
HEIGHT = 720


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    
    # Render game here

    pygame.display.flip()

    clock.tick(60) # Limits FPS to 60

pygame.quit()


