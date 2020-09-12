import pygame


pygame.font.init()

# game constants
FPS = 60  # game speed
WIDTH = 1280  # screen width
HEIGHT = 800  # screen height
white = (255, 255, 255)

# text variables


font_variable = pygame.font.Font('freesansbold.ttf', 30)


def redrawWindow(win, b, p1, p2, p_sc, op_sc):
    """
    :param win:   main window
    :param b:     ball
    :param p1:    player_1
    :param p2:    player_2/opponent
    :param p_sc:  player_score
    :param op_sc: opponent_score
    """
    win.fill((51, 51, 51))
    pygame.draw.aaline(win, white, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    b.draw(win)
    p1.draw(win)
    p2.draw(win)

    # score
    player_text = font_variable.render(f'{p_sc}', False, white)
    opponent_text = font_variable.render(f'{op_sc}', False, white)
    win.blit(player_text, (660, 40))
    win.blit(opponent_text, (600, 40))

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


def score(obj):
    if obj.x <= 0:
        player_score +=1
        obj.reset_pos()
    elif obj.x + obj.width >= WIDTH:
        opponent_score +=1
        obj.reset_pos()
    else:
        return False
