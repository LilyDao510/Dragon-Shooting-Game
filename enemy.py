import pygame

from screen import screen, screen_rect
from background import background
from config import scale


class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed) -> None:
        super().__init__()
        self.images = [pygame.image.load('sprite/enemy/0.png').convert_alpha(), 
                       pygame.image.load('sprite/enemy/1.png').convert_alpha(),
                       pygame.image.load('sprite/enemy/2.png').convert_alpha(),
                       pygame.image.load('sprite/enemy/3.png').convert_alpha(),
                       pygame.image.load('sprite/enemy/4.png').convert_alpha(),
                       pygame.image.load('sprite/enemy/5.png').convert_alpha()]
        self.image = pygame.image.load('sprite/enemy/0.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.offset = (int(self.rect.x),int(self.rect.y))
        self.rect.x = screen_rect.width/2 - background.rect.width/2 + 25
        self.rect.y = float(0)
        self.stage = 0
        self.speed = float(speed)
        
    def update(self):
        screen.blit(self.images[int(self.stage/5)], self.rect)
        self.stage += 1
        if self.stage > 25:
            self.stage = 0
        self.rect.y = float(self.rect.y + self.speed)
        






