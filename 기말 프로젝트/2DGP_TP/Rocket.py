import gfw
from pico2d import *
import gobj


class rocket:
    def __init__(self, x, y, dir, dx, dy):
        self.pos = [x, y]
        self.dir = dir
        self.image = gfw.load_image(gobj.RES_DIR + 'Rocket.png')
        self.acc = 0.3
        self.dx = dx
        self.dy = dy

        if dir == 0:
            self.dx = -1 + self.dx
        elif dir == 1:
            self.dx = 1 + self.dx
        elif dir == 2:
            self.dy = 1 + self.dy
        elif dir == 3:
            self.dy = -1 + self.dy

    def draw(self):
        width, height = 32, 32
        sx = 0
        sy = 0

        if self.dir == 0:
            self.image.clip_draw(sx, sy, width, height, self.pos[0], self.pos[1], 64, 64)
        elif self.dir == 1:
            self.image.clip_composite_draw(sx, sy, width, height, 0, 'h', self.pos[0], self.pos[1], 64, 64)
        elif self.dir == 2:
            self.image.clip_composite_draw(sx, sy, width, height, -3.141592 / 2, '', self.pos[0], self.pos[1], 64, 64)
        elif self.dir == 3:
            self.image.clip_composite_draw(sx, sy, width, height, 3.141592 / 2, '', self.pos[0], self.pos[1], 64, 64)

    def update(self):
        if self.dir == 0:
            self.dx = self.dx - self.acc
        elif self.dir == 1:
            self.dx = self.dx + self.acc
        elif self.dir == 2:
            self.dy = self.dy + self.acc
        elif self.dir == 3:
            self.dy = self.dy - self.acc

        self.pos[0] = self.dx + self.pos[0]
        self.pos[1] = self.dy + self.pos[1]

        if self.pos[0] > get_canvas_width() or self.pos[1] > get_canvas_height() or self.pos[0] < 0 or self.pos[1] < 0:
            self.remove()

    def remove(self):
        gfw.world.remove(self)
