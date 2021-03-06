import gfw
from pico2d import *
import gobj
import math


class tail:
    def __init__(self, x, y, Offset):
        self.pos = [x, y]
        self.image = gfw.load_image(gobj.RES_DIR + 'RocketTail.png')
        self.fidx = 0
        self.stime = 0
        self.isOffset = Offset

    def draw(self):
        width, height = 16, 16
        sx = self.fidx * 16
        sy = 0

        self.image.clip_draw(sx, sy, width, height, self.pos[0], self.pos[1], 10, 10)

    def update(self):
        self.stime += gfw.delta_time

        for i in range(3):
            if self.stime > 0.1 * i / 3:

                if self.isOffset:
                    self.fidx = i

                else:
                    self.fidx = i + 3

        if self.stime > 0.2:
            self.remove()

    def remove(self):
        gfw.world.remove(self)

def play_hit():
    global hitsound
    hitsound = load_wav('sound/missile_hit.wav')
    hitsound.set_volume(64)
    hitsound.play()

class rocket:

    LRBB = [-16, -8, 16, 8]
    UDBB = [-8, -16, 8, 16]

    def __init__(self, x, y, dir, dx, dy):
        self.toff = 0
        self.pos = [x, y]
        self.dir = dir
        self.image = gfw.load_image(gobj.RES_DIR + 'Rocket.png')
        self.acc = 8
        self.dx = dx
        self.dy = dy

        self.xOffset = 0
        self.yOffset = 0

        if dir == 0:
            self.dx = -10 + self.dx
        elif dir == 1:
            self.dx = 10 + self.dx
        elif dir == 2:
            self.dy = 10 + self.dy
        elif dir == 3:
            self.dy = -10 + self.dy

    def draw(self):
        width, height = 32, 32
        sx = 0
        sy = 0

        if self.dir == 0:
            self.image.clip_draw(sx, sy, width, height, self.pos[0], self.pos[1], 32, 32)
        elif self.dir == 1:
            self.image.clip_composite_draw(sx, sy, width, height, 0, 'h', self.pos[0], self.pos[1], 32, 32)
        elif self.dir == 2:
            self.image.clip_composite_draw(sx, sy, width, height, -3.141592 / 2, '', self.pos[0], self.pos[1], 32, 32)
        elif self.dir == 3:
            self.image.clip_composite_draw(sx, sy, width, height, 3.141592 / 2, '', self.pos[0], self.pos[1], 32, 32)

    def update(self):
        if self.dir == 0:
            self.dx += (self.dx - self.acc) * gfw.delta_time
            t = tail(self.pos[0] + 10, self.pos[1], self.toff)
            gfw.world.add(gfw.layer.effect, t)

        elif self.dir == 1:
            self.dx += (self.dx + self.acc) * gfw.delta_time
            t = tail(self.pos[0] - 10, self.pos[1], self.toff)
            gfw.world.add(gfw.layer.effect, t)

        elif self.dir == 2:
            self.dy += (self.dy + self.acc) * gfw.delta_time
            t = tail(self.pos[0], self.pos[1] - 10, self.toff)
            gfw.world.add(gfw.layer.effect, t)

        elif self.dir == 3:
            self.dy += (self.dy - self.acc) * gfw.delta_time
            t = tail(self.pos[0], self.pos[1] + 10, self.toff)
            gfw.world.add(gfw.layer.effect, t)

        self.pos[0] = self.dx + self.pos[0]
        self.pos[1] = self.dy + self.pos[1]

        for p in gfw.world.objects_at(gfw.layer.player):
            self.xOffset = p.xOffset
            self.yOffset = p.yOffset

        if self.toff:
            self.toff = False
        else:
            self.toff = True

        if self.pos[0] > get_canvas_width() or self.pos[1] > get_canvas_height() or self.pos[0] < 0 or self.pos[1] < 0:
            self.remove()
        for p in gfw.world.objects_at(gfw.layer.platform):
            l, b, r, t = p.get_bb()
            l -= self.xOffset
            b -= self.yOffset
            r -= self.xOffset
            t -= self.yOffset

            if l < self.pos[0] < r and t > self.pos[1] > b:
                for pl in gfw.world.objects_at(gfw.layer.player):
                    if math.sqrt(pow(pl.pos[0] - self.pos[0], 2) + pow(pl.pos[1] - self.pos[1], 2)) < 100\
                            and self.pos[1] < pl.pos[1] - 10:
                        pl.delta = pl.delta[0], 3

                self.remove()

    def remove(self):
        play_hit()
        gfw.world.remove(self)

    def get_bb(self):
        l, b, r, t = 0, 0, 0, 0
        if self.dir == 0 or self.dir == 1:
            l, b, r, t = rocket.LRBB
        elif self.dir == 2 or self.dir == 3:
            l, b, r, t = rocket.UDBB

        x, y = self.pos
        return x + l + self.xOffset, y + b + self.yOffset, x + r + self.xOffset, y + t + self.yOffset
