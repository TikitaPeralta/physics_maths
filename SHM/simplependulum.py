import pygame, sys, math
from pygame.locals import QUIT

ORIGIN = (200, 150)
RADIUS = 70
bob = [ORIGIN[0], ORIGIN[1] + RADIUS]

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('SHM')

Clock = pygame.time.Clock()

while True:
    Clock.tick(60)
    current_time = pygame.time.get_ticks()
  
    DISPLAYSURF.fill((0,0,0))
    pygame.draw.line(DISPLAYSURF, (255,255,255), ORIGIN, bob)
    pygame.draw.circle(DISPLAYSURF, 255, bob, 7)
    current_time_milliseconds_as_fraction = current_time/1000.0
    

    bob[0] = ORIGIN[0] + (math.sin(current_time_milliseconds_as_fraction)  * RADIUS)
    bob[1] = ORIGIN[1] + abs(math.cos(current_time_milliseconds_as_fraction) * RADIUS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()