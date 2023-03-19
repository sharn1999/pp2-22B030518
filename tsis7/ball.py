import pygame
pygame.init()
RES = WIDTH, HEIGHT = 300, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))

done = False
clock = pygame.time.Clock()
posX = 50
posY = 50

UP_key = pygame.K_UP
DOWN_key = pygame.K_DOWN
RIGHT_key = pygame.K_RIGHT
LEFT_key = pygame.K_LEFT

while not done:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == UP_key:
                if(posY>50):
                    posY -= 20
                else:
                    pass
            elif event.key == DOWN_key:
                if(posY<HEIGHT-51):
                    posY += 20
                else:
                    pass
            elif event.key == LEFT_key:
                if(posX>50):
                    posX -= 20
                else:
                    pass
            elif event.key == RIGHT_key:
                if(posX<=WIDTH-51):
                    posX += 20
                else:
                    pass
    screen.fill((255,255,255))
    pygame.draw.circle(screen, 'red', (posX, posY), 50)
    clock.tick(30)
pygame.quit()       
exit()