import pygame
from utility import WIDTH, HEIGHT


class GameObject():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def update(self):
        """
        update rect after moving it
        """
        self.rect = (self.x, self.y, self.width, self.height)


class Player(GameObject):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.vel = 5
        self.points = 0

    def move(self):
        """
        moving Player object up and down with keys
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y > 10:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y < (HEIGHT - (10 + self.height)):
            self.y += self.vel

        self.update()


# ball object
class Ball(GameObject):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.vel_x = 5
        self.vel_y = 5

    def draw(self, window):
        pygame.draw.ellipse(window, self.color, self.rect)

    def move(self):
        """
        move Ball object with a fixed velocity,
        after running to the end of frame, change direction
        """
        self.y += self.vel_y
        self.x += self.vel_x

        if self.y <= 10 or (self.y + self.height) >= HEIGHT:
            self.vel_y *= -1

        self.update()

    def collide(self):
        self.vel_x *= -1

    def off_screen(self):
        if self.x <= 0 or self.x + self.width >= WIDTH:
            return True

    def reset_pos(self):
        self.x = WIDTH / 2 - 15
        self.y = HEIGHT / 2 - 15
        self.update()


class Opponent(GameObject):
    def __init__(self, x, y, width, height, color, vel):
        super().__init__(x, y, width, height, color)
        self.vel = vel
        self.points = 0

    def ai_movement(self, b):
        """
        arg: b - ball\n
        moves according to ball's y position
        """
        if self.y + self.vel + self.height <= HEIGHT and self.y - self.vel > 10:
            if self.y < b.y:
                self.y += self.vel
            if self.y + self.height > b.y + b.height:
                self.y -= self.vel
        self.update()
