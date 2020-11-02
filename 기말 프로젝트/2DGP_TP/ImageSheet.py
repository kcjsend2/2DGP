import random
from pico2d import *
import gfw
import gobj

UNIT = 64

class ImageSheet:
    UNIT = 64

    def __init__(self, width, height, slice, file):
        self.width = width
        self.hegiht = height
        self.slice = slice
        self.ImageSheet = gfw.load_image(gobj.RES_DIR + file)

    def update(self): pass

    def draw(self):
        self.image.draw_to_origin(self.left, self.bottom, self.width, self.height)

    def get_bb(self):
        return self.left, self.bottom, self.left + self.width, self.bottom + self.height
