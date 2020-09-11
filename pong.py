from objects import *
from utility import *

# pyGame essentials
pygame.init()
clock = pygame.time.Clock()

# main window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong:The Game')


# creating game obj
ball = Ball(WIDTH / 2 - 15, HEIGHT / 2 - 15, 30, 30, white)
player = Player(WIDTH - 20, HEIGHT / 2 - 70, 10, 120, white)
opponent = Player(10, HEIGHT / 2 - 70, 10, 120, white)


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
        if check_collision_player(ball, player) or check_collision_opponent(ball, opponent):
            ball.collide()
        redrawWindow(WINDOW, ball, player, opponent)


main()
