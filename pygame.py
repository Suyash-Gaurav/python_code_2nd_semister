import pygame
import time
import os


def main():
    pygame.init()
    main_surface = pygame.display.set_mode((480, 240))
    pygame.display.set_caption('Pygame Example')

    ball_path = "ball.png"
    if not os.path.exists(ball_path):
        print(f"Error: The file '{ball_path}' does not exist.")
        return

    ball = pygame.image.load(ball_path)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        main_surface.fill((0, 200, 255))
        main_surface.fill((255, 0, 0), (300, 100, 150, 90))
        main_surface.blit(ball, (100, 120))
        pygame.display.flip()

        clock.tick(30)  # Control the frame rate to 30 FPS

    pygame.quit()


main()


