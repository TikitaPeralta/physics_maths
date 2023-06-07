import pygame

W, H = 500, 600
black = (0, 0, 0)
white = (255, 255, 255)

def play():
    pygame.init()
    display = pygame.Surface((W, H))
    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()

    run = True
    velocity = 10