import pygame

W, H = 500, 600
black = (0, 0, 0)
white = (255, 255, 255)

def play():
    pygame.init()
    display = pygame.Surface((W, H))
    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    velocity = 10
    circle_x = 100
    circle_y = 300

    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        screen.fill(black)
        
        pygame.draw.circle(screen, white, [circle_x, circle_y], 10)


        display.blit(screen, (0,0))
        pygame.display.update()
        
    pygame.quit()

play()