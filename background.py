import pygame
import math

from screen import screen_rect, screen

class Background:
    def __init__(self) -> None:
        self.image = pygame.transform.scale(pygame.image.load("sprite/background/pink.jpg"), (500,screen_rect.height - 200)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = screen_rect.center
        self.tiles = math.ceil(screen_rect.height/self.rect.height) + 1
        self.speed = 0

    def update(self):
        self.scroll()
        for i in range(-1, self.tiles):
            screen.blit(self.image, (self.rect.x, i*self.rect.width + self.speed))

    def scroll(self):
        self.speed += 2
        if abs(self.speed) > self.rect.width:
            self.speed = 0


background = Background()