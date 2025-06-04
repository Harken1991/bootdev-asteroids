import pygame
from constants import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
black = (0, 0, 0)


def starting_asteroids():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


screen.fill(black)
pygame.display.flip()


starting_asteroids()

if __name__ == "__main__":
    main()
