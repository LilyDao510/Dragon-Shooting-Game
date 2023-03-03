import pygame

from screen import screen, screen_rect

class Button(pygame.sprite.Sprite):
    def __init__(self) -> None:
        self.image = pygame.image.load('sprite/button/0.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = screen_rect.center
        self.mask = pygame.mask.from_surface(self.image)
        self.text_color = (30, 30, 30)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.score = 0

    def update(self):
        self.score_image = self.font.render(str(self.score), True, self.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.center = screen_rect.center
        self.score_rect.y += (self.rect.height/3)
        screen.blit(self.image, self.rect)
        screen.blit(self.score_image, self.score_rect)

    def update_score(self, score):
        self.score = score