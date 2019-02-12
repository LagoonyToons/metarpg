import pygame as pg
from options import *

class Camera:
    def __init__(self, target, world_size):
        self.target = target
        self.cam = pg.Vector2(0, 0)
        self.world_size = world_size

    def update(self, target):
        x = -self.target.rect.center[0] + SCREEN_X / 2
        y = -self.target.rect.center[1] + SCREEN_Y / 2
        #print(x)
        self.cam += (pg.Vector2((x, y)) - self.cam) * 0.05
        #print(self.cam)
        self.cam.x = max(-(self.world_size[0] - SCREEN_X),
                         min(0, self.cam.x))
        self.cam.y = max(-(self.world_size[1] - SCREEN_Y),
                         min(0, self.cam.y))

    def draw(self, screen, objectList):
        for obj in objectList:
           # print(obj.x)
           # print(self.cam.x)
            if obj.rect.x < -self.cam.x+SCREEN_X and obj.rect.x+obj.rect.width > -self.cam.x and obj.rect.y < -self.cam.y+SCREEN_Y and obj.rect.y+obj.rect.height > -self.cam.y:
                obj.draw(screen, obj.rect.x+self.cam.x, obj.rect.y+self.cam.y)