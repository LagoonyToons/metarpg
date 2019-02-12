import pygame as pg
from options import *
from camera import *
from player import *
from wall import *
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
        self.entities = []
        self.walls = []
        self.genMap()
        self.entities.append(self.player)

        width = (len(self.level[0])*TILE_SIZE)
        length = (len(self.level)*TILE_SIZE)
        self.camera = Camera(self.player, (width, length))

        self.gameLoop()

    def gameLoop(self):
        while True:
            self.controls()
            self.camera.update(self.player)
            self.camera.draw(self.screen, self.entities)
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
                self.player.moveCount = 5
            elif pressed[pg.K_d]:
                self.player.move(1,0,self.walls)
                self.player.moveCount = 5
            elif pressed[pg.K_w]:
                self.player.move(0,-1,self.walls)
                self.player.moveCount = 5
            elif pressed[pg.K_s]:
                self.player.move(0,1,self.walls)
                self.player.moveCount = 5
        else:
            self.player.moveCount -= 1

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
                else:
                    block = Block((x, y))
                    self.entities.append(block)
                x += TILE_SIZE
            y += TILE_SIZE
            x = 0

    def loadImages(self):
        self.playerImage = pg.transform.scale(pg.image.load(IMAGE_PATH + "player.png"), (80, 80))
        
Game()