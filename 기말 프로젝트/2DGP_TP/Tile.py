from pico2d import *
import gfw
import gobj


class Tile:
    xOffset = 0
    yOffset = 0

    def __init__(self, x, y, sx, sy, isCollision, isFlag):
        self.width = 32
        self.height = 32
        self.tpos = [x / 32, y / 32]
        self.pos = [x, y]
        self.image = gfw.image.load(gobj.RES_DIR + '/PrtWhite.png')
        self.sPos = sx, sy
        self.CollisionMode = isCollision
        self.isFlag = isFlag

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw_to_origin(*self.sPos, self.width, self.height, self.pos[0] - Tile.xOffset, self.pos[1] - Tile.yOffset)

    def dictionary(self):
        x, y = self.pos
        sx, sy = self.sPos
        return {"x": x, "y": y, "sx": sx, "sy": sy, "isCollision": self.CollisionMode, "isFlag": self.isFlag}

    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        if self.CollisionMode:
            x, y = self.pos
            return x, y, x + 32, y + 32
        else:
            return 0, 0, 0, 0