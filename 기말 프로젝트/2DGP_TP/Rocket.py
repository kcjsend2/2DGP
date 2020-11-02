import gfw
from pico2d import *
import gobj


class rocket:
    def __init__(self, x, y, dir):
        self.pos = [x, y]
        self.dir = dir
        self.image = gfw.load_image(gobj.RES_DIR + 'Rocket.png')
        self.acc = 0.3
        if dir == 0:
            self.dx = -1
        elif dir == 3:
            self.dx = 1

    def draw(self):
        width, height = 32, 32
        sx = 0
        sy = 0

        if self.dir == 0:
            self.image.clip_draw(sx, sy, width, height, self.pos[0] - 20, self.pos[1], 64, 64)
        elif self.dir == 3:
            self.image.clip_composite_draw(sx, sy, width, height, 0, 'h', self.pos[0] + 20, self.pos[1], 64, 64)

    def update(self):
        if self.dir == 0:
            self.dx = self.dx - self.acc
        elif self.dir == 3:
            self.dx = self.dx + self.acc

        self.pos[0] = self.dx + self.pos[0]

