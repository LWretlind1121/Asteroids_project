import pygame
import random
from constants import *
from main import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (128, 128, 128), self.position, self.radius, 0)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        vector1 = pygame.Vector2(self.position.x, self.position.y).rotate(random_angle)
        vector2 = pygame.Vector2(self.position.x, self.position.y).rotate(-random_angle)
        self.radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)

        asteroid1.velocity = vector1 * 1.2
        asteroid2.velocity = vector2 * 1.2