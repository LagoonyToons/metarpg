import pygame as pg
from options import *
from camera import *
from player import *
from wall import *
from enemy import *
from battle import *
import sys

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((SCREEN_X, SCREEN_Y))
        pg.display.set_caption("METAR PG 13")

        self.loadImages()
        self.clock = pg.time.Clock()
        self.player = Player(100, 100, self.playerImage)
        self.playerList = [self.player]
        self.entities = []
        self.walls = []
        self.enemies = []
        self.genMap()
        self.entities.append(self.player)
        self.drawCamera()

        width = (len(self.level[0])*TILE_SIZE)
        length = (len(self.level)*TILE_SIZE)
        self.camera = Camera(self.player, (width, length))

        self.gameLoop()

    def gameLoop(self):
        while True:
            self.controls()
            self.camera.update(self.player)
            self.camera.draw(self.screen, self.entities)
            battleTime = self.player.update(self.enemies)
            if battleTime:
                print(len(self.enemies))
                Battle(self.playerList, self.enemies, self.screen)
            self.drawHUD()
            pg.display.update()
            self.screen.fill(pg.Color("black"))
            self.clock.tick(60)

    def controls(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                sys.exit()
        pressed = pg.key.get_pressed()
        if self.player.moveCount == 0:
            if pressed[pg.K_a]:
                self.player.move(-1,0,self.walls)
                self.player.moveCount = 2
            elif pressed[pg.K_d]:
                self.player.move(1,0,self.walls)
                self.player.moveCount = 2
            elif pressed[pg.K_w]:
                self.player.move(0,-1,self.walls)
                self.player.moveCount = 2
            elif pressed[pg.K_s]:
                self.player.move(0,1,self.walls)
                self.player.moveCount = 2
        else:
            self.player.moveCount -= 1

    def drawHUD(self):
        for row in self.rowList:
            for col in row:
                self.screen.blit(col[0], col[1])
        pg.draw.circle(self.screen, pg.Color("lightblue"), (round(
            self.player.rect.x/self.compression)+SCREEN_X-200, round(self.player.rect.y/self.compression)), 2)
        
    def drawCamera(self):
        totalSize_x = 150
        totalSize_y = 100
        self.compression = 8
        x = SCREEN_X-(round(TILE_SIZE/self.compression)*len(self.level[0]))
        y = 0
        self.rowList = []
        for row in self.level:
            columnList = []
            for col in row:
                item = []
                if col == "P":
                    # pg.draw.rect(self.screen, pg.Color("red"), [
                    #              x, y, round(TILE_SIZE/compression), round(TILE_SIZE/compression)])
                    rect = pg.Surface(
                        (round(TILE_SIZE/self.compression), round(TILE_SIZE/self.compression)), pg.SRCALPHA, 32)
                    rect.fill((0, 0, 255, 128))
                    item.append(rect)
                    item.append((x, y))
                    #self.screen.blit(rect, (x, y))
                elif col == "E":
                    rect = pg.Surface(
                        (round(TILE_SIZE/self.compression), round(TILE_SIZE/self.compression)), pg.SRCALPHA, 32)
                    rect.fill((255, 0, 0, 128))
                    item.append(rect)
                    item.append((x, y))
                else:
                    rect = pg.Surface(
                        (round(TILE_SIZE/self.compression), round(TILE_SIZE/self.compression)), pg.SRCALPHA, 32)
                    rect.fill((0,0,0,128))
                    item.append(rect)
                    item.append((x, y))
                    #self.screen.blit(rect, (x, y))
                columnList.append(item)
                x += round(TILE_SIZE/self.compression)
            self.rowList.append(columnList)
            y += round(TILE_SIZE/self.compression)
            x = SCREEN_X-(round(TILE_SIZE/self.compression)*len(self.level[0]))
        

    def genMap(self):
        with open("map.txt", "r") as f:
            self.level = f.readlines()
            f.close()
        x = y = 0
        for row in self.level:
            for col in row:
                if col == "P":
                    wall = Wall((x, y))
                    self.walls.append(wall)
                    self.entities.append(wall)
                elif col == "E":
                    enemy = Enemy(x, y, self.enemyImage)
                    self.enemies.append(enemy)
                    print(len(self.enemies))
                    self.entities.append(enemy)
                else:
                    block = Block((x, y))
                    self.entities.append(block)
                x += TILE_SIZE
            y += TILE_SIZE
            x = 0

    def loadImages(self):
        self.playerImage = pg.transform.scale(pg.image.load(IMAGE_PATH + "player.png"), (80, 80))
        self.enemyImage = pg.transform.scale(
            pg.image.load(IMAGE_PATH + "player.png"), (80, 80))
        
Game()
