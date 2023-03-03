import pygame
from config import screen_width, screen_height

pygame.display.set_caption("Dragon Shooter")
screen = pygame.display.set_mode((screen_width,screen_height))
screen_rect = screen.get_rect()