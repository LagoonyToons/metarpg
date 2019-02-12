import pygame as pg 
from options import *
import random

class Battle:
    def __init__(self, players, enemies, screen):
        self.screen = screen
        self.players = players
        self.enemies = enemies
        self.entities = []

        for player in self.players:
            self.entities.append(player)
        for enemy in self.enemies:
            self.entities.append(enemy)

        self.totalMovement = 20

        self.gameLoop()

    def gameLoop(self):
        print(len(self.enemies))
        dead = False
        while not dead:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    sys.exit()
            self.moveSpeed()
            self.screenHandler()
            dead = self.isDead()
    
    def screenHandler(self):
        pass

    def moveSpeed(self):
        total = 0
        for entity in self.entities:
            total += entity.battle_speed

        for entity in self.entities:
            entity.battle_y -= round(entity.battle_speed/total)
            if entity.battle_y <= 0:
                entity.turn(self.enemies, self.players)
        
    def isDead(self):
        enemy_deathCount = 0
        player_deathCount = 0
        for enemy in self.enemies:
            if enemy.hp > 0:
                break
            else: enemy_deathCount += 1
        for player in self.players:
            if player.hp > 0:
                break
            else:
                player_deathCount += 1
        if player_deathCount >= len(self.players) or enemy_deathCount >= len(self.enemies) and enemy_deathCount > 0:
            return True
        else:
            return False
