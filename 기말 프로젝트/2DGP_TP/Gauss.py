import gfw
from pico2d import *
import gobj

class Gauss:
    def __init__(self, x, y, dir):
        self.pos = [x, y]
        self.image = gfw.load_image(gobj.RES_DIR + 'GaussBullet.png')
        self.dir = dir
        if self.dir == 0:
            self.dx = -5000
            self.dy = 0
        elif self.dir == 1:
            self.dx = 5000
            self.dy = 0
        elif self.dir == 2:
            self.dx = 0
            self.dy = 5000
        elif self.dir == 3:
            self.dx = 0
            self.dy = -5000

    def draw(self):
        width, height = 64, 4
        sx = 0
        sy = 0

        if self.dir == 0:
            self.image.clip_draw(sx, sy, width, height, self.pos[0], self.pos[1], 128, 8)
        elif self.dir == 1:
            self.image.clip_composite_draw(sx, sy, width, height, 0, 'h', self.pos[0], self.pos[1], 128, 8)
        elif self.dir == 2:
            self.image.clip_composite_draw(sx, sy, width, height, -3.141592 / 2, '', self.pos[0], self.pos[1], 128, 8)
        elif self.dir == 3:
            self.image.clip_composite_draw(sx, sy, width, height, 3.141592 / 2, '', self.pos[0], self.pos[1], 128, 8)

    def update(self):
        self.pos[0] = self.dx * gfw.delta_time + self.pos[0]
        self.pos[1] = self.dy * gfw.delta_time + self.pos[1]

        if self.pos[0] > get_canvas_width() or self.pos[1] > get_canvas_height() or self.pos[0] < 0 or self.pos[1] < 0:
            self.remove()

    def remove(self):
        gfw.world.remove(self)