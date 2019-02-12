import pygame as pg
from options import *
from pygame import *

class Wall:
    def __init__(self, pos):
        self.image = Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(pg.Color("orange"))
        self.rect = self.image.get_rect(topleft=pos)

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))

class Block:
    def __init__(self, pos):
        self.image = Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(pg.Color("brown"))
        self.rect = self.image.get_rect(topleft=pos)
    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))