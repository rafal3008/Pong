from objects import *

# pyGame essentials
pygame.init()
clock = pygame.time.Clock()
# game constants
FPS = 60
WIDTH = 1280  # screen width
HEIGHT = 800  # screen height

# main window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong:The Game')

white = (255, 255, 255)
# creating game obj
ball = Ball(WIDTH / 2 - 15, HEIGHT / 2 - 15, 30, 30, white)
player = Player(WIDTH - 20, HEIGHT / 2 - 70, 10, 120, white)
opponent = Player(10, HEIGHT / 2 - 70, 10, 120, white)


def redrawWindow(b, p1, p2):
    WINDOW.fill((51, 51, 51))
    pygame.draw.aaline(WINDOW, white, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    b.draw(WINDOW)
    p1.draw(WINDOW)
    p2.draw(WINDOW)
    pygame.display.update()


def main():
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player.move()
        ball.move()
        redrawWindow(ball, player, opponent)


main()
