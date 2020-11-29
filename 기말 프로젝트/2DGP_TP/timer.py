from pico2d import *
import gfw
from gobj import *
import time


class Timer:
    def __init__(self, right, y):
        self.stime = time.time()
        self.right, self.y = right, y
        self.image = gfw.image.load(RES_DIR + '/number_24x32.png')
        self.digit_width = self.image.w // 10
        self.now = 0

    def draw(self):
        x = self.right
        sec = int(self.now)
        minute = sec // 60
        sec -= minute * 60

        scnt = 0
        while sec > 0:
            digit = sec % 10
            sx = digit * self.digit_width
            x -= self.digit_width
            self.image.clip_draw(sx, 0, self.digit_width, self.image.h, x, self.y)
            sec //= 10
            scnt += 1

        if scnt == 0:
            for i in 0, 1:
                x -= self.digit_width
                self.image.clip_draw(0, 0, self.digit_width, self.image.h, x, self.y)

        if 0 < scnt < 2:
            while scnt > 0:
                scnt -= 1
                x -= self.digit_width
                self.image.clip_draw(0, 0, self.digit_width, self.image.h, x, self.y)

        x -= 10
        mcnt = 0
        while minute > 0:
            digit = minute % 10
            sx = digit * self.digit_width
            x -= self.digit_width
            self.image.clip_draw(sx, 0, self.digit_width, self.image.h, x, self.y)
            minute //= 10
            mcnt += 1

        if mcnt == 0:
            for i in 0, 1:
                x -= self.digit_width
                self.image.clip_draw(0, 0, self.digit_width, self.image.h, x, self.y)

        if 0 < mcnt < 2:
            while mcnt > 0:
                mcnt -= 1
                x -= self.digit_width
                self.image.clip_draw(0, 0, self.digit_width, self.image.h, x, self.y)

    def get_time(self):
        return self.now

    def update(self):
        self.now = time.time() - self.stime
