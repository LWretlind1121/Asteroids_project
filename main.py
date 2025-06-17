import pygame
import sys
from player import *
from asteroid import *
from asteroidfield import *
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawbles = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawbles)
    Asteroid.containers = (asteroids, updatables, drawbles)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawbles, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatables.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid) == True:
                    shot.kill()
                    asteroid.split()
            if asteroid.collision(player) == True:
                sys.exit("Game over!")
                

        screen.fill("black")

        for draw in drawbles:
            draw.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
