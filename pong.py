import pygame

WIDTH = 500
HEIGHT = 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong:The Game')


def redrawWindow():
    WIN.fill((255, 255, 255))
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    FPS = 60

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        redrawWindow()

main()
