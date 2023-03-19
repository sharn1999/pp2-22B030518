import pygame
import datetime
from time import sleep


pygame.init()
RES = WIDTH, HEIGHT = 1400, 700
H_WIDTH, H_HEIGHT = WIDTH//2, HEIGHT//2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
clock60 = dict(zip(range(60), range(0, 360, 6)))

image1 = pygame.image.load('arm11.png')
image2 = pygame.image.load('arm22.png')


done = False

def main(a,b, img, angle):
    image_rect = img.get_rect(topleft = ((pos[0] +a)/2, (pos[1]-b)/2))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle*1)
    rotated_image_center = ((pos[0] - rotated_offset.x), (pos[1] - rotated_offset.y))
    rotated_image = pygame.transform.rotate(img, angle*1)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
    screen.blit(rotated_image, rotated_image_rect)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pos = (screen.get_width()/2, screen.get_height()/2)

    micky_surf = pygame.image.load('main-clock.png')
    micky_rect = micky_surf.get_rect(topleft = (290,-70))
    screen.blit(micky_surf, micky_rect)


    t = datetime.datetime.now()
    minute, second = (t.minute, t.second)
    angle1 = 0
    angle1 -= clock60[second]
    angle2 = 0
    angle2 -= clock60[minute]

    main(655, 195, image1, angle1)
    main(650, 70, image2, angle2)

    pygame.display.flip()
    sleep(1)
pygame.quit()       
exit()