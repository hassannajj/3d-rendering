import pygame
import sys

class Player:
    def __init__(self, x, y, radius, speed):
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.speed = speed
        self.color = 'white'

    def update_pos(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.position.y -= self.speed * dt
        if keys[pygame.K_s]:
            self.position.y += self.speed * dt
        if keys[pygame.K_a]:
            self.position.x -= self.speed * dt
        if keys[pygame.K_d]:
            self.position.x += self.speed * dt

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)


class Simulation:
    def __init__(self):
        # Pygame setup
        pygame.init()
        self.width = WIDTH
        self.height = HEIGHT
        self.bg_color = BG_COLOR

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

        self.player = Player(WIDTH / 2, HEIGHT / 2, RADIUS, SPEED)

    def handle_events(self):
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False

    def update(self):
        self.player.update_pos(self.dt)

    def draw(self):
        self.screen.fill(self.bg_color)
        self.player.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.dt = self.clock.tick(60) / 1000

        pygame.quit()
        sys.exit();


# CONSTANTS
WIDTH = 1280
HEIGHT = 720
RADIUS = 50
SPEED = 200
BG_COLOR = "blue"

if __name__ == "__main__":
    simulation = Simulation()
    simulation.run()
