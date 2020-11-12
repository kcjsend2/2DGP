import random
from pico2d import *
import gfw
import gobj
from Rocket import *
from Gauss import *


class Player:
    KEYDOWN_Z = (SDL_KEYDOWN, SDLK_z)
    KEYDOWN_X = (SDL_KEYDOWN, SDLK_x)
    KEYDOWN_LEFT = (SDL_KEYDOWN, SDLK_LEFT)
    KEYDOWN_RIGHT = (SDL_KEYDOWN, SDLK_RIGHT)
    KEYDOWN_UP = (SDL_KEYDOWN, SDLK_UP)
    KEYDOWN_DOWN = (SDL_KEYDOWN, SDLK_DOWN)
    KEYUP_LEFT = (SDL_KEYUP, SDLK_LEFT)
    KEYUP_RIGHT = (SDL_KEYUP, SDLK_RIGHT)
    KEYUP_UP = (SDL_KEYUP, SDLK_UP)
    KEYUP_DOWN = (SDL_KEYUP, SDLK_DOWN)
    KEYDOWN_A = (SDL_KEYDOWN, SDLK_a)
    KEYDOWN_S = (SDL_KEYDOWN, SDLK_s)

    KEYDOWN_SPACE  = (SDL_KEYDOWN, SDLK_SPACE)
    KEYDOWN_LSHIFT = (SDL_KEYDOWN, SDLK_LSHIFT)
    KEYUP_LSHIFT   = (SDL_KEYUP,   SDLK_LSHIFT)

    image = None
    weaponImage = None

    isUp = False
    isDown = False
    isLeft = False
    isRight = False
    isFalling = False
    gravity = 6

    SelectedWeapon = 1

    Boots = True
    Rocketlauncher = True
    GaussGun = True

    BB = [-16, -16, 16, 16]

    #constructor
    def __init__(self):
        self.GaussDelay = 1.0
        self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.delta = 0, 0
        self.target = None
        self.speed = 200
        self.delay_frame = 12
        self.image = gfw.image.load(gobj.RES_DIR + '/MyChar.png')
        self.weaponImage = gfw.image.load(gobj.RES_DIR + '/Arms.png')
        self.time = 0
        self.fidx = 0
        self.jumpCount = 0
        self.isWalk = False
        self.isJumping = False
        self.action = 2
        self.velocity = 0, 0

    def draw(self):
        width, height = 32, 32
        sx = 0
        sy = 0

        if self.action == 0:
            sy = 1 * height
            if self.isWalk:
                if self.fidx % 2 != 0:
                    sx = (int)((self.fidx + 1) / 2 * width)
                else:
                    sx = 0

        elif self.action == 1:
            sy = 0 * height
            if self.isWalk:
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

        weaponWidth = 36
        weaponHeight = 13
        flip = ''
        rad = 0
        xoffSet = 8
        yoffset = 0


        if self.action == 2 or self.action == 0:
            if self.isUp is True:
                rad = -3.141592 / 2
                yoffset = -20
                if self.isJumping:
                    sx = 5 * width
            if self.isDown is True and self.isJumping is True:
                rad = 3.141592 / 2
                yoffset = 20
                sx = 6 * width


        if self.action == 3 or self.action == 1:
            flip = 'h'
            xoffSet = -8
            if self.isUp is True:
                rad = 3.141592 / 2
                yoffset = -20
                if self.isJumping:
                    sx = 5 * width
            if self.isDown is True and self.isJumping is True:
                rad = -3.141592 / 2
                yoffset = 20
                sx = 6 * width


        if self.SelectedWeapon != 0:
            self.weaponImage.clip_composite_draw((self.SelectedWeapon - 1) * weaponWidth, 0,
                                                 weaponWidth * self.SelectedWeapon, weaponHeight,
                                                 rad, flip, self.pos[0] - xoffSet, self.pos[1] - 3 - yoffset, 36, 13)

        if self.isUp is True and self.isJumping is False:
            sx += width * 3

        self.image.clip_draw(sx, sy, width, height, *self.pos, 32, 32)

    def update(self):
        if Player.isRight and self.delta[0] < 1.0:
            self.delta = gobj.point_add(self.delta, (0.06, 0))

        if Player.isLeft and self.delta[0] > -1.0:
            self.delta = gobj.point_add(self.delta, (-0.06, 0))

        if not Player.isRight and self.delta[0] > 0:
            self.delta = gobj.point_add(self.delta, (-0.06, 0))
            if self.delta[0] < 0.1:
                self.delta = (0, self.delta[1])

        if not Player.isLeft and self.delta[0] < 0:
            self.delta = gobj.point_add(self.delta, (0.06, 0))
            if self.delta[0] > -0.1:
                self.delta = (0, self.delta[1])

        #타일과 충돌처리 필요
        if self.pos[1] > 100:
            self.isFalling = 1

        elif self.pos[1] < 100:
            self.pos = (self.pos[0], 100)
            self.isFalling = False
            self.isJumping = False

            if self.Boots:
                self.jumpCount = 2
            else:
                self.jumpCount = 1

            self.delta = (self.delta[0], 0)

        if self.isFalling:
            self.delta = (self.delta[0], self.delta[1] - self.gravity * gfw.delta_time)

        x, y = self.pos
        dx, dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time
        self.delay_frame -= 1

        self.pos = x, y

        self.time += gfw.delta_time
        frame = self.time * 15

        if dx < 0 or dx > 0:
            self.isWalk = True
        else:
            self.isWalk = False

        if self.isWalk:
            if self.delay_frame == 0 and not self.isJumping:
                self.fidx += 1
                if self.fidx % 4 == 0:
                    self.fidx = 0
            if self.isJumping:
                if self.fidx == 0 or self.fidx == 2:
                    self.fidx = 1

        else:
            self.fidx = 0

        if self.delay_frame == 0:
             self.delay_frame = 12

        if self.GaussDelay < 1.5:
            self.GaussDelay += gfw.delta_time
        else:
            self.GaussDelay = 1.5

    def fire(self):
        if self.SelectedWeapon == 1 and self.GaussDelay == 1.5:
            self.GaussDelay = 0
            if self.action == 0 or self.action == 2:
                g = Gauss(self.pos[0] - 50, self.pos[1], 0)

                if not self.isUp and not self.isDown:
                    self.delta = self.delta[0] + 3, self.delta[1]
                elif self.isUp:
                    self.delta = self.delta[0], self.delta[1] - 0.5
                elif self.isDown:
                    self.delta = self.delta[0], self.delta[1] + 0.5

                if self.isUp is True:
                    g = Gauss(self.pos[0], self.pos[1] + 50, 2)
                if self.isDown is True and self.isJumping is True:
                    g = Gauss(self.pos[0], self.pos[1] - 50, 3)

            elif self.action == 1 or self.action == 3:
                g = Gauss(self.pos[0] + 50, self.pos[1], 1)

                if not self.isUp and not self.isDown:
                    self.delta = self.delta[0] - 3, self.delta[1]
                elif self.isUp:
                    self.delta = self.delta[0], self.delta[1] - 0.5
                elif self.isDown:
                    self.delta = self.delta[0], self.delta[1] + 0.5

                if self.isUp is True:
                    g = Gauss(self.pos[0], self.pos[1] + 50, 2)
                if self.isDown is True and self.isJumping is True:
                    g = Gauss(self.pos[0], self.pos[1] - 50, 3)

            gfw.world.add(gfw.layer.bullet, g)

        if self.SelectedWeapon == 2 and gfw.world.count_at(1) < 3:
            if self.action == 0 or self.action == 2:
                b = rocket(self.pos[0] - 50, self.pos[1], 0, self.velocity[0], 0)
                if self.isUp is True:
                    b = rocket(self.pos[0], self.pos[1] + 50, 2, 0, self.velocity[1])
                if self.isDown is True and self.isJumping is True:
                    b = rocket(self.pos[0], self.pos[1] - 50, 3, 0, -self.velocity[1])

            elif self.action == 1 or self.action == 3:
                b = rocket(self.pos[0] + 50, self.pos[1], 1, self.velocity[0], 0)
                if self.isUp is True:
                    b = rocket(self.pos[0], self.pos[1] + 50, 2, 0, self.velocity[1])
                if self.isDown is True and self.isJumping is True:
                    b = rocket(self.pos[0], self.pos[1] - 50, 3, 0, -self.velocity[1])

            gfw.world.add(gfw.layer.bullet, b)

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair == Player.KEYDOWN_RIGHT:
            self.action = 1
            Player.isRight = True
            if Player.isLeft:
                Player.isLeft = False

        elif pair == Player.KEYUP_RIGHT:
            if self.action == 1:
                self.action = 3
            Player.isRight = False

        elif pair == Player.KEYDOWN_LEFT:
            self.action = 0
            Player.isLeft = True
            if Player.isRight:
                Player.isRight = False

        elif pair == Player.KEYUP_LEFT:
            if self.action == 0:
                self.action = 2
            Player.isLeft = 0

        elif pair == Player.KEYDOWN_UP:
            Player.isUp = True
        elif pair == Player.KEYUP_UP:
            Player.isUp = False

        elif pair == Player.KEYDOWN_DOWN:
            Player.isDown = True
        elif pair == Player.KEYUP_DOWN:
            Player.isDown = False

        elif pair == Player.KEYDOWN_Z:
            if self.jumpCount > 0:
                self.jumpCount -= 1
                self.isJumping = True
                self.delta = (self.delta[0], 2.0)

        elif pair == Player.KEYDOWN_A:
            if self.Rocketlauncher:
                self.SelectedWeapon = 2
        elif pair == Player.KEYDOWN_S:
            if self.GaussGun:
                self.SelectedWeapon = 1
        elif pair == Player.KEYDOWN_X:
            self.fire()

    def get_bb(self):
        l, b, r, t = Player.BB
        x, y = self.pos
        return x + l, y + b, x + r, y + t
