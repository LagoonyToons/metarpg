import pygame as pg

class Enemy:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.battle_speed = 5
        self.battle_y = 100
        self.hp = 10

    def turn(self, enemies, players):
        players[0].hp -= 1
        print(players[0].hp)

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))

    
