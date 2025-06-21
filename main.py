import pygame, sys
from constants import *
from circleshape import *
from player import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield  = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for u in updatable:
            u.update(dt)

        for a in asteroids:
            if a.collides(player):
                print("Game over!")
                sys.exit()
            for s in shots:
                if s.collides(a):
                    a.split()
                    s.kill

        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
