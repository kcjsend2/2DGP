import gfw
from pico2d import *
from gobj import *


class Background:
    def __init__(self, imageName, t_max_x, t_max_y):
        self.imageName = imageName
        self.image = gfw.image.load(res(imageName))
        self.cw, self.ch = t_max_x, t_max_y
        self.win_rect = 0, 0, self.cw, self.ch
        self.center = self.image.w // 2, self.image.h // 2
        hw, hh = self.cw // 2, self.    ch // 2
        self.boundary = hw, hh, self.image.w - hw, self.image.h - hh

    def draw(self):
        x, y = 0, 0
        for pl in gfw.world.objects_at(gfw.layer.player):
            px, py = pl.pos
            xOffset = pl.xOffset
            yOffset = pl.yOffset
        dx, dy = x - px - xOffset, y - py - yOffset
        self.image.draw_to_origin(x + dx * 0.05, y + dy * 0.05, self.cw, self.ch)

    def update(self):
        pass