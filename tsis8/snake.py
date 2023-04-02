import pygame
import random
pygame.init()
yellow = (255, 255, 102)
black = (0, 0, 0)
dis_width = 600
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
clock = pygame.time.Clock()
snake_block = 32
snake_speed = 8
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
background = pygame.image.load('ground.png')

def Your_score(score):
    value = score_font.render(str(score), True, yellow)
    dis.blit(value, [70, 10])
    
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def gameLoop():
    game_over = False
    game_close = False
    x1 = 9 * snake_block
    y1 = 10 * snake_block
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = random.randrange(1,17) * 32
    foody = random.randrange(3, 15) * 32

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 < snake_block or x1 > snake_block*17 or y1 > 17*snake_block or y1 < 3 * snake_block:
            game_close = True
        while game_close == True:
            dis.blit(background, (0, 0))

            Your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        x1 += x1_change
        y1 += y1_change
        dis.blit(background, (0, 0))

        carrot = pygame.image.load('carrot.png')
        image_rect = carrot.get_rect(topleft = (foodx, foody))
        dis.blit(carrot, image_rect)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
                foodx = random.randrange(1,17) * 32
                foody = random.randrange(3, 15) * 32
                Length_of_snake += 1
        clock.tick(8)
    pygame.quit()
    quit()
gameLoop()