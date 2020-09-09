import pygame

# pyGame essentials
pygame.init()
clock = pygame.time.Clock()
# game constants
FPS = 60
WIDTH = 1280  # screen width
HEIGHT = 960  # screen height

# main window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong:The Game')


# player object
class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 5

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    # def move(self):
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_UP]:
    #         self.y -= self.vel
    #     if keys[pygame.K_DOWN]:
    #         self.y += self.vel
    #


# ball object
class Ball():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

white = (255,255,255)
# creating game obj
ball = Ball(WIDTH / 2 - 15, HEIGHT / 2 - 15, 30, 30, white)
player = Player(WIDTH - 20, HEIGHT/2 - 70, 10, 140, white)
opponent = Player(10, HEIGHT/2 - 70, 10, 140, white)


def redrawWindow(win, b, p1, p2):
    win.fill((51, 51, 51))
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

        redrawWindow(WINDOW)


main()
