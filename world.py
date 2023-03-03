import pygame
import sys
from time import sleep

from config import bg_color, speed, scale
from screen import screen, screen_rect
from background import background
from dragon import dragon
from enemy import Enemy
from button import Button
from score import Scoreboard

class World:
    def __init__(self) -> None:
        self.active = False
        self.dragons = 2
        self.enemies = pygame.sprite.Group()
        self.create_enemy()
        self.start_button = Button()
        self.score = Scoreboard()

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Tat man hinh
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    dragon.move_right = True
                elif event.key == pygame.K_LEFT:
                    dragon.move_left = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    dragon.move_right = False
                elif event.key == pygame.K_LEFT:
                    dragon.move_left = False
                if event.key == pygame.K_SPACE:
                    dragon.shoot()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

        self._check_enemy_collide_bullet()

        self._check_dragon_hit()
        
        self.check_enemy_bottom()

        self._check_clear_round()

    def update(self):
        screen.fill(bg_color)
        background.update()
        self.score.update()
        dragon.update()
        self.enemies.update()
    
    def draw_start_screen(self):
        screen.fill(bg_color)
        background.update()
        self.start_button.update()

    def create_enemy(self):
        global speed
        for i in range(4):
            for j in range(5):
                enemy = Enemy(float(speed))
                enemy.rect.x += j*(enemy.rect.width + 20)
                enemy.rect.y += i*(enemy.rect.height + 10)
                self.enemies.add(enemy)

    def _dragon_hit(self):
        if self.dragons > 0:
            self.dragons -= 1
            self.restart_world()
            sleep(0.5)
        else:
            self.start_button.update_score(self.score.score)
            self.active = False

    def check_enemy_bottom(self):
        for enemy in self.enemies.sprites():
            if enemy.rect.bottom >= screen_rect.bottom:
                self._dragon_hit()
                break
    
    def restart_world(self):
        self.enemies.empty()
        dragon.bullets.empty()
        self.create_enemy()
        dragon.center_dragon()

    def _check_play_button(self, mouse_pos):
        if self.start_button.rect.collidepoint(mouse_pos):
            self.active = True
            self.reset_stat()
    
    def _check_clear_round(self):
        global speed, scale
        if len(self.enemies) == 0:
            speed = speed*1.2
            dragon.bullets.empty()
            self.create_enemy()
            self.enemies.sprites
    
    def _check_dragon_hit(self):
        if pygame.sprite.spritecollideany(dragon, self.enemies):
            self._dragon_hit()

    def _check_enemy_collide_bullet(self):
        collide = pygame.sprite.groupcollide(self.enemies, dragon.bullets, True, True)
        if collide:
            self.score.increase_score()

    def reset_stat(self):
        global speed
        speed = 1
        self.dragons = 2
        self.score.reset_score()

world = World()