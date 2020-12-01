import gfw
from pico2d import *
import gobj

class item:
    def __init__(self, x, y, type):
        self.pos = [x, y]
        self.type = type
        self.image = gfw.image.load(gobj.RES_DIR + '/Arms.png')

        self.CollisionMode = True
        self.isFlag = False

    def draw(self):
        weaponWidth = 36
        self.image.clip_draw(self.type * weaponWidth, 0, 36, 13, self.pos[0], self.pos[1])

    def dictionary(self):
        x, y = self.pos
        return {"x": x, "y": y, "type": self.type}

    def remove(self):
        gfw.world.remove(self)

    def update(self):
        pass

    def get_bb(self):
        if self.CollisionMode:
            x, y = self.pos
            return x, y, x + 32, y + 32
        else:
            return 0, 0, 0, 0