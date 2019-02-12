import pygame as pg
from options import *

class Player:
    def __init__(self, x, y, img):
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.moveAmount = TILE_SIZE
        self.moveCount = 0

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
        screen.blit(self.img, (x, y))