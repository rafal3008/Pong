import pygame

# game constants
FPS = 60  # game speed
WIDTH = 1280  # screen width
HEIGHT = 800  # screen height
white = (255, 255, 255)


def redrawWindow(win, b, p1, p2):
    win.fill((51, 51, 51))
    pygame.draw.aaline(win, white, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    b.draw(win)
    p1.draw(win)
    p2.draw(win)
    pygame.display.update()


def check_collision_player(b, p):
    """
    b: ball object \n
    p: player object\n
    check if ball's hitbox collide with player's hitbox\n
    returns boolean
    """
    if b.x + b.width == p.x and b.y >= p.y and (b.y + b.height) <= (p.y + p.height):
        return True


def check_collision_opponent(b, op):
    """
    b: ball object\n
    op: opponent object\n
    check if ball's hitbox collide with opponent's hitbox \n
    returns boolean
    """
    if b.x == op.x + op.width and b.y >= op.y and (b.y + b.height) <= (op.y + op.height):
        return True

