import pygame
from constants import *


class Player:
    def __init__(self, start_pos):
        self.position = pygame.Vector2(start_pos[0], start_pos[1])
    

    def get_next_pos(self, dt):
        new_x = self.position.x
        new_y = self.position.y

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            new_y -= (SPEED * dt)
        if keys[pygame.K_s]:
            new_y += (SPEED * dt)
        if keys[pygame.K_a]:
            new_x -= (SPEED * dt)
        if keys[pygame.K_d]:
            new_x += (SPEED * dt)

        return new_x, new_y


    def update_pos(self, pos):
        self.position.x = pos[0]
        self.position.y = pos[1]

    def get_curr_pos(self):
        return self.position


    def draw(self, screen):
        pygame.draw.circle(screen, 
                           PLAYER_COLOR, 
                           (int(self.position.x), 
                           int(self.position.y)), 
                           RADIUS)
