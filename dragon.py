import pygame

from screen import screen, screen_rect
from background import background
from bullet import Bullet


class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        self.images = [pygame.transform.scale(pygame.image.load("sprite/dragon/0.png"), (95,80)).convert_alpha(),
                       pygame.transform.scale(pygame.image.load("sprite/dragon/1.png"), (95,80)).convert_alpha(),
                       pygame.transform.scale(pygame.image.load("sprite/dragon/2.png"), (95,80)).convert_alpha(),
                       pygame.transform.scale(pygame.image.load("sprite/dragon/3.png"), (95,80)).convert_alpha(),
                       pygame.transform.scale(pygame.image.load("sprite/dragon/4.png"), (95,80)).convert_alpha(),
                       pygame.transform.scale(pygame.image.load("sprite/dragon/5.png"), (95,80)).convert_alpha()]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.midbottom = screen_rect.midbottom
        self.move_right = False
        self.move_left = False
        self.stage = 0
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.move()
        # Draw screen
        screen.blit(self.images[int(self.stage/5)], self.rect)
        self.bullets.update()
        # Animation
        self.stage += 1
        if self.stage > 25:
            self.stage = 0
        # Delete old bullet      
        for bullet in self.bullets:
            if bullet.out() == True:
                self.bullets.remove(bullet)

    def move(self):
        if self.move_right == True:
            self.rect.x = self.rect.x + 5
        if self.move_left == True:
            self.rect.x = self.rect.x - 5
        self.boundary()

    def shoot(self):
        bullet = Bullet(self.rect)
        self.bullets.add(bullet)
    
    def center_dragon(self):
        self.rect.midbottom = screen_rect.midbottom
    
    def boundary(self):
        if self.rect.x > ((screen_rect.width/2)+(background.rect.width/2)-self.rect.width):
            self.rect.x -= 5
        if self.rect.x < ((screen_rect.width/2)-(background.rect.width/2)):
            self.rect.x += 5

dragon = Dragon()
