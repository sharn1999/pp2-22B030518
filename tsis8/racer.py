import random

import pygame

pygame.init()
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
SCORE = 0
COINS = 0
clock = pygame.time.Clock()
background = pygame.image.load('AnimatedStreet.png')
score_font = pygame.font.SysFont("Verdana", 30)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.image = pygame.image.load('Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.width, WIDTH - self.rect.width),0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if self.rect.y > HEIGHT:
            SCORE += 1
            self.speed += 1
            self.rect.center = (random.randint(self.rect.width, WIDTH - self.rect.width),0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 8
        self.image = pygame.image.load('Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.move_ip(-self.speed, 0)
        elif pressed[pygame.K_RIGHT] and self.rect.right <= WIDTH:
            self.rect.move_ip(self.speed, 0)
        elif pressed[pygame.K_UP] and self.rect.top >= 0:
            self.rect.move_ip(0, -self.speed)
        elif pressed[pygame.K_DOWN] and self.rect.bottom <= HEIGHT:
            self.rect.move_ip(0, self.speed)
    def Coins(self):
        global posCoin
        global COINS
        coin = pygame.image.load('coin.png')
        image_rect = coin.get_rect(topleft = (posCoin[0], posCoin[1]))
        if(self.rect.left <= posCoin[0] and self.rect.right >= posCoin[0] and self.rect.top<=posCoin[1] and self.rect.bottom>=posCoin[1]):
            posCoin = (random.randint(0, WIDTH-50), random.randint(HEIGHT//2,HEIGHT-100))
            COINS += 1
        SCREEN.blit(coin, image_rect)
posCoin = (random.randint(0, WIDTH-30), random.randint(HEIGHT/1.2,HEIGHT-100))

def main():
    running = True
    player = Player()
    enemy = Enemy()
    enemies = pygame.sprite.Group()
    enemies.add(enemy)


    while running:
        SCREEN.blit(background, (0, 0))
        score = score_font.render(f" Your score: {SCORE}", True, (0, 0, 0))
        SCREEN.blit(score, (0, 0))
        coins = score_font.render(f" Your coins: {COINS}", True, (0, 0, 0))
        SCREEN.blit(coins, (0, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update()
        enemy.update()
        player.Coins()

        player.draw(SCREEN)
        enemy.draw(SCREEN)
        if pygame.sprite.spritecollideany(player, enemies):
            running = False
        pygame.display.flip()
        clock.tick(100)


if __name__ == '__main__':
    main()