import pygame
import sys
from player import Player
from maze import Maze
from ray import Ray
from constants import *



maze_arr = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
]



class Simulation:
    def __init__(self):
        # Pygame setup
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.mouse_pos = (0, 0) 


        self.maze = Maze(maze_arr)
        start_pos = self.maze.get_first_0() 
        self.player = Player(start_pos)
        self.ray = Ray(start_pos, self.mouse_pos)



    def handle_events(self):
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False


    def moveIsValid(self, pos):
        return not self.maze.is_wall(pos[0], pos[1])


    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()

        next_player_pos = self.player.get_next_pos(self.dt)
        if self.moveIsValid(next_player_pos):
            self.player.update_pos(next_player_pos)
            self.ray.update(next_player_pos, self.mouse_pos)



    def draw(self):
        self.screen.fill(BG_COLOR)
        self.maze.draw(self.screen)
        self.player.draw(self.screen)
        self.ray.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.dt = self.clock.tick(60) / 1000

        pygame.quit()
        sys.exit();


if __name__ == "__main__":
    simulation = Simulation()
    simulation.run()
