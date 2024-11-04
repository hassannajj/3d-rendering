import pygame
from constants import *

class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        self.cell_size = WIDTH / len(grid)

    def draw(self, screen):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 1:
                    cell = pygame.Rect(int(j*self.cell_size), int(i*self.cell_size), self.cell_size, self.cell_size),
                    pygame.draw.rect(screen, 'black', cell)

    def is_wall(self, x, y):
        col = int(x // self.cell_size)
        row = int(y // self.cell_size)
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col] == 1
        return True  # Outside bounds are considered walls

    def get_first_0(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 0:
                    return int(i*self.cell_size) + RADIUS, int(j*self.cell_size) + RADIUS
