import pygame as pg
from options import *
from battle import *

class Player:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.moveAmount = 10
        self.moveCount = 0

        self.battle_speed = 5
        self.battle_y = 100
        self.hp = 10

    def turn(self, enemies, players):
        enemies[0].hp -= 1

    def adjustY(self, changeAmount):
        self.battle_y = self.battle_y - changeAmount

    def update(self, enemies):
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                if enemy.hp > 0:
                    return True
                else:
                    enemies.remove(enemy)

    def move(self, x, y, walls):
        self.rect.x += self.moveAmount*x
        self.rect.y += self.moveAmount*y
        self.collide(x, y, walls)

    def collide(self, x, y, walls):
        for p in walls:
            if pg.sprite.collide_rect(self, p):
                if x > 0:
                    self.rect.right = p.rect.left
                if x < 0:
                    self.rect.left = p.rect.right
                if y > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.y = 0
                if y < 0:
                    self.rect.top = p.rect.bottom
    
    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))
