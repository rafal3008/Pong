import pygame

# window sizes
HEIGHT = 800
WIDTH = 1280


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
        update Player object after moving it
        """
        self.rect = (self.x, self.y, self.width, self.height)


class Player(GameObject):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.vel = 5

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

        if self.y <= 0 or (self.y + self.height) >= HEIGHT:
            self.vel_y *= -1
        if self.x <= 0 or (self.x + self.width) >= WIDTH:
            self.vel_x *= -1

        self.update()
