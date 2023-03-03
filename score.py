import pygame

from screen import screen
from background import background

pygame.init()

class Scoreboard:
    def __init__(self):
        self.text_color = (30, 30, 30)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.score = 0

    def update(self):
        self.score_image = self.font.render(str(self.score), True, self.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = background.rect.right - 10
        self.score_rect.y = 10
        screen.blit(self.score_image, self.score_rect)

    def increase_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0
