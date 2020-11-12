from pico2d import *
import gfw
import gobj

class Tile:
    def __init__(self, x, y, sx, sy, w, h, isCollision):
        self.width = w
        self.height = h
        self.pos = [x, y]
        self.image = self.image = gfw.image.load(gobj.RES_DIR + '/PrtWhite.png')
        self.sPos = sx, sy
        self.CollisionMode = isCollision

    def draw(self):
        self.image.clip_draw(*self.sPos, self.width, self.height, *self.pos)