import pygame

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
