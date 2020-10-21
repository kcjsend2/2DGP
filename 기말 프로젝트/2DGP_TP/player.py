import random
from pico2d import *
import gfw
import gobj


class Player:
    KEYDOWN_Z = (SDL_KEYDOWN, SDLK_z)
    KEYDOWN_LEFT = (SDL_KEYDOWN, SDLK_LEFT)
    KEYDOWN_RIGHT = (SDL_KEYDOWN, SDLK_RIGHT)
    KEYUP_LEFT = (SDL_KEYUP, SDLK_LEFT)
    KEYUP_RIGHT = (SDL_KEYUP, SDLK_RIGHT)

    KEYDOWN_SPACE  = (SDL_KEYDOWN, SDLK_SPACE)
    KEYDOWN_LSHIFT = (SDL_KEYDOWN, SDLK_LSHIFT)
    KEYUP_LSHIFT   = (SDL_KEYUP,   SDLK_LSHIFT)
    image = None
    isLeft = 0
    isRight = 0
    isFalling = 0
    gravity = 0.08

    #constructor
    def __init__(self):
        self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.delta = 0, 0
        self.target = None
        self.speed = 200
        self.delay_frame = 12
        self.image = gfw.image.load(gobj.RES_DIR + '/MyChar.png')
        self.time = 0
        self.fidx = 0
        self.jumpCount = 2
        self.isWalk = 0
        self.isJumping = 0
        self.action = 2
        self.velocity = 0, 0

    def draw(self):
        width, height = 32, 32
        sx = 0
        sy = 0

        if self.action == 0:
            sy = 1 * height
            if self.isWalk == 1:
                if self.fidx % 2 != 0:
                    sx = (int)((self.fidx + 1) / 2 * width)
                else:
                    sx = 0

        elif self.action == 1:
            sy = 0 * height
            if self.isWalk == 1:
                if self.fidx % 2 != 0:
                    sx = (int)((self.fidx + 1) / 2 * width)
                else:
                    sx = 0

        elif self.action == 2:
            sy = 1 * height
            sx = 0
        elif self.action == 3:
            sy = 0 * height
            sx = 0

        if self.delta[1] > 0:
            sx = 8 * width

        self.image.clip_draw(sx, sy, width, height, *self.pos, 64, 64)

    def update(self):
        if Player.isRight == 1 and self.delta[0] < 1.5:
            self.delta = gobj.point_add(self.delta, (0.03, 0))

        if Player.isLeft == 1 and self.delta[0] > -1.5:
            self.delta = gobj.point_add(self.delta, (-0.03, 0))

        if Player.isRight == 0 and self.delta[0] > 0:
            self.delta = gobj.point_add(self.delta, (-0.03, 0))
            if self.delta[0] < 0.1:
                self.delta = (0, self.delta[1])

        if Player.isLeft == 0 and self.delta[0] < 0:
            self.delta = gobj.point_add(self.delta, (0.03, 0))
            if self.delta[0] > -0.1:
                self.delta = (0, self.delta[1])

        if self.pos[1] > 100:
            self.isFalling = 1

        elif self.pos[1] < 100:
            self.pos = (self.pos[0], 100)
            self.isFalling = 0
            self.isJumping = 0
            self.jumpCount = 2
            self.delta = (self.delta[0], 0)

        if self.isFalling:
            self.delta = (self.delta[0], self.delta[1] - self.gravity)

        x, y = self.pos
        dx, dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time
        self.delay_frame -= 1

        self.pos = x, y

        self.time += gfw.delta_time
        frame = self.time * 15

        if dx < 0 or dx > 0:
            self.isWalk = 1
        else:
            self.isWalk = 0

        if self.isWalk == 1:
            if self.delay_frame == 0 and self.isJumping == 0:
                self.fidx += 1
                if self.fidx % 4 == 0:
                    self.fidx = 0
            if self.isJumping == 1:
                if self.fidx == 0 or self.fidx == 2:
                    self.fidx = 1

        else:
            self.fidx = 0

        if (self.delay_frame == 0):
             self.delay_frame = 12

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair == Player.KEYDOWN_RIGHT:
            self.action = 1
            Player.isRight = 1
            if Player.isLeft == 1:
                Player.isLeft = 0

        elif pair == Player.KEYUP_RIGHT:
            if self.action == 1:
                self.action = 3
            Player.isRight = 0

        elif pair == Player.KEYDOWN_LEFT:
            self.action = 0
            Player.isLeft = 1
            if Player.isRight == 1:
                Player.isRight = 0

        elif pair == Player.KEYUP_LEFT:
            if self.action == 0:
                self.action = 2
            Player.isLeft = 0

        elif pair == Player.KEYDOWN_Z:
            if self.jumpCount > 0:
                self.jumpCount -= 1
                self.isJumping = 1
                self.delta = (self.delta[0], 2)

    def get_bb(self):
        hw = 20
        hh = 40
        x, y = self.pos
        return x - hw, y - hh, x + hw, y + hh
