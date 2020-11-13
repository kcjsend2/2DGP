from pico2d import *
import gfw
import gobj

class Tile:
    def __init__(self, x, y, sx, sy, w, h, isCollision):
        self.width = w
        self.height = h
        self.tpos = [x / 32, y / 32]
        self.pos = [x, y]
        self.image = self.image = gfw.image.load(gobj.RES_DIR + '/PrtWhite.png')
        self.sPos = sx, sy
        self.CollisionMode = isCollision

    def draw(self):
        self.image.clip_draw_to_origin(*self.sPos, self.width, self.height, *self.pos)

    def dictionary(self):
        x, y = self.pos
        return {"x": x, "y": y, "sx": self.sx, "sy": self.sy, "w": self.w, "h": self.h, "isCollision": self.CollisionMode}
