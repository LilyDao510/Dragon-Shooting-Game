import pygame

from screen import screen

class Bullet(pygame.sprite.Sprite):
    def __init__(self, rect) -> None:
        super().__init__()
        self.images = [pygame.transform.scale(pygame.image.load('sprite/bullet/0.png').convert_alpha(),(50,50)),
                       pygame.transform.scale(pygame.image.load('sprite/bullet/1.png').convert_alpha(),(50,50)),
                       pygame.transform.scale(pygame.image.load('sprite/bullet/2.png').convert_alpha(),(50,50)),
                       pygame.transform.scale(pygame.image.load('sprite/bullet/3.png').convert_alpha(),(50,50)),
                       pygame.transform.scale(pygame.image.load('sprite/bullet/4.png').convert_alpha(),(50,50)),
                       pygame.transform.scale(pygame.image.load('sprite/bullet/5.png').convert_alpha(),(50,50))]
        self.image = pygame.image.load('sprite/bullet/0.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = rect.x + 25
        self.rect.y = rect.y - 25
        self.stage = 0

    def update(self):
        screen.blit(self.images[int(self.stage/5)], self.rect)
        self.stage += 1
        if self.stage > 25:
            self.stage = 0
        self.rect.y -= 10

    def out(self):
        if self.rect.y < 0 - self.rect.height:
            return True