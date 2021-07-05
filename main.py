import pygame as pg
import numpy as np
import random
import noise

class Game:
    A_NOP, A_UP, A_DOWN, A_LEFT, A_RIGHT, A_ATK = range(6)

    def __init__(self):
        self.framerate = 10
        self.width, self.height = (16, 16)
        self.scale = 16
        pg.init()
        self.screen = pg.display.set_mode((self.width * self.scale, self.height * self.scale))
        self.clock = pg.time.Clock()
        self.player = Player((self.width // 2, self.height // 2), self)
        self.map = np.zeros((self.width, self.height))
        self.generate_world()

    def step(self, action):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pg.event.pump()
        self.player.move(action)

    def render(self, mode='human'):
        # Background
        pg.draw.rect(self.screen, (24, 24, 24), (0, 0, self.width * self.scale, self.height * self.scale))
        
        for i in range(self.width):
            for j in range(self.height):
                pg.draw.rect(self.screen, (64, (128 + self.map[i][j] * 128) % 256, 64), (i * self.scale, j * self.scale, self.scale, self.scale))
        
        # Player
        pg.draw.rect(self.screen, (200, 24, 24), (self.player.x * self.scale, self.player.y * self.scale, self.scale, self.scale))

            
        pg.display.flip()
        self.clock.tick(int(self.framerate))
    
    def generate_world(self):
        # Simple perlin noise

        scale = 10
        octaves = 6
        persistence = 0.5
        lacunarity = 2.0

        for i in range(self.width):
            for j in range(self.height):
                self.map[i][j] = noise.pnoise2(
                    i / scale, 
                    j / scale, 
                    octaves=octaves, 
                    persistence=persistence, 
                    lacunarity=lacunarity, 
                    repeatx=self.width, 
                    repeaty=self.height, 
                    base=0
                )

class Player:
    DIR_S, DIR_W, DIR_N, DIR_E = range(4)

    def __init__(self, init_pos, world):
        self.x, self.y = init_pos
        self.facing = Player.DIR_S
        self.world = world # To get collision info

    def move(self, action):
        if action == Game.A_UP:
            if self.facing == self.DIR_N:
                self.y = (self.y - 1) % self.world.height
            else:
                self.facing = self.DIR_N

        if action == Game.A_DOWN:
            if self.facing == self.DIR_S:
                self.y = (self.y + 1) % self.world.height
            else:
                self.facing = self.DIR_S
        
        if action == Game.A_LEFT:
            if self.facing == self.DIR_W:
                self.x = (self.x - 1) % self.world.height
            else:
                self.facing = self.DIR_W

        if action == Game.A_RIGHT:
            if self.facing == self.DIR_E:
                self.x = (self.x + 1) % self.world.height
            else:
                self.facing = self.DIR_E
            
game = Game()

while True:
    game.step(random.choice([Game.A_UP, Game.A_DOWN, Game.A_LEFT, Game.A_RIGHT]))
    game.render()