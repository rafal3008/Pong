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
opponent = Opponent(10, HEIGHT / 2 - 70, 10, 120, white, 4)


def main():
    run = True
    # scores
    player_score = 0
    opponent_score = 0

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player.move()
        ball.move()
        opponent.ai_movement(ball)
        if check_collision_player(ball, player) or check_collision_opponent(ball, opponent):
            ball.collide()
            score(ball)
        if ball.off_screen():
            if ball.x <= 0:
                player_score += 1
            elif ball.x + ball.width >= WIDTH:
                opponent_score += 1
            ball.reset_pos()

        redrawWindow(WINDOW, ball, player, opponent, player_score, opponent_score)


main()
