import pygame

# window sizes
HEIGHT = 800
WIDTH = 1280


class Player:
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

    def move(self):
        '''
        moving object up and down with keys
        '''
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y > 10:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y < (HEIGHT - (10 + self.height)):
            self.y += self.vel

        self.update()

    def update(self):
        '''
        update object after moving it
        '''
        self.rect = (self.x, self.y, self.width, self.height)


# ball object
class Ball:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.ellipse = (x, y, width, height)
        self.vel_x = 5
        self.vel_y = 5

    def draw(self, window):
        pygame.draw.ellipse(window, self.color, self.ellipse)

    def move(self):
        self.x +=self.vel_x
        self.y +=self.vel_y
        self.update()

    def update(self):
        self.ellipse = (self.x, self.y, self.width, self.height)
