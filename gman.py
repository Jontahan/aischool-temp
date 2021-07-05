import os
import pygame as pg

class GraphicsManager:
    def __init__(self):
        pwd = os.path.dirname(os.path.realpath(__file__))
        self.scale = 16
        tile_sheet = pg.image.load(os.path.join(pwd, 'res', 'rogueliketiles.png'))
        creature_sheet = pg.image.load(os.path.join(pwd, 'res', 'roguelikecreatures.png'))
        
        self.sprites = {
            'tree' : self.get_tile(tile_sheet, 0, 0),
            'wall' : self.get_tile(tile_sheet, 1, 1),
            'person' : self.get_tile(creature_sheet, 0, 0),
            'skeleton' : self.get_tile(creature_sheet, 0, 6)
        }

    def get_tile(self, sheet, x, y):
        tile = pg.Surface((self.scale, self.scale), pg.SRCALPHA)
        tile.blit(sheet, (0, 0), pg.Rect(self.scale * x, self.scale * y, self.scale, self.scale))
        return tile
