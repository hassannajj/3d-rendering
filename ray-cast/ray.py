import pygame
from constants import *

class Ray:
    def __init__(self, player_pos, mouse_pos):
        self.player_pos = pygame.Vector2(player_pos[0], player_pos[1])
        self.mouse_pos = pygame.Vector2(mouse_pos[0], mouse_pos[1])
        self.rays = []


    def draw(self, screen):
        # Draws 90 lines in a triangle shape
        
        print(self.mouse_pos)
        num_lines = 30
        for i in range(num_lines + 1):
            # Interpolate along the left and right base points
            left_point = (
                self.mouse_pos[0]-100 + (self.player_pos[0] - self.mouse_pos[0]-100) * i / num_lines,
                self.mouse_pos[1]-100 + (self.player_pos[1] - self.mouse_pos[1]-100) * i / num_lines
            )
#             right_point = (
#                 self.mouse_pos[0]+100 + (self.player_pos[0] - self.mouse_pos[0]+100) * i / num_lines,
#                 self.mouse_pos[1]+100 + (self.player_pos[1] - self.mouse_pos[1]+100) * i / num_lines
#             )
            
            pygame.draw.line(screen, 'yellow', self.player_pos, left_point)
#             pygame.draw.line(screen, 'yellow', self.player_pos, right_point)


#         pygame.draw.polygon(screen, 
#                            "yellow", 
#                                 [self.player_pos, 
#                                 [self.mouse_pos[0]-100, self.mouse_pos[1]], 
#                                 [self.mouse_pos[0]+100, self.mouse_pos[1]]]
#                             )



    def update(self, player_pos, mouse_pos):
        self.player_pos = player_pos
        self.mouse_pos = mouse_pos
