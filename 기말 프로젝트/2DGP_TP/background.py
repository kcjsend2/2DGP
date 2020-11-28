import gfw
from pico2d import *
from gobj import *


class Background:
    def __init__(self, imageName, t_max_x, t_max_y):
        self.imageName = imageName
        self.image = gfw.image.load(res(imageName))
        self.target = None
        self.cw, self.ch = t_max_x, t_max_y
        self.win_rect = 0, 0, self.cw, self.ch
        self.center = self.image.w // 2, self.image.h // 2
        hw, hh = self.cw // 2, self.    ch // 2
        self.boundary = hw, hh, self.image.w - hw, self.image.h - hh

    def set_target(self, target):
        self.target = target
        self.update()

    def draw(self):
        self.image.clip_draw_to_origin(*self.win_rect, 0, 0)

    def update(self):
        if self.target is None:
            return
        tx, ty = self.target.pos
        sl = round(tx - self.cw / 2)
        sb = round(ty - self.ch / 2)
        self.win_rect = sl, sb, self.cw, self.ch

    def get_boundary(self):
        return self.boundary

    def translate(self, point):
        x, y = point
        l, b, r, t = self.win_rect
        return l + x, b + y

    def to_screen(self, point):
        # return self.cw // 2, self.ch // 2
        x, y = point
        l, b, r, t = self.win_rect
        return x - l, y - b