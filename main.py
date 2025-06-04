import pygame
from constants import *

# setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
black = (0, 0, 0)
clock = pygame.time.Clock()
dt = 0


def starting_asteroids():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        print(f"Delta time (seconds): {dt}")


screen.fill(black)
pygame.display.flip()

# start game loop
starting_asteroids()

if __name__ == "__main__":
    main()
