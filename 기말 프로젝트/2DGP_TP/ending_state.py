import random
from pico2d import *
import gfw
import gobj
import time

canvas_width = 1280
canvas_height = 960

global ntime
global font
global display
global image

def enter():
    global stime
    stime = time.time()

    global ntime
    ntime = 0

    global font
    font = gfw.font.load(gobj.RES_DIR + 'ENCR10B.TTF', 30)

    global now
    for t in gfw.world.objects_at(gfw.layer.ui):
        if hasattr(t, 'now'):
            now = t.now

    global ending
    ending = load_music('sound/ending.ogg')
    ending.set_volume(32)
    ending.repeat_play()

    global image
    image = gfw.image.load(gobj.RES_DIR + '/WhiteSpace.png')

    global total
    total = 0
    for i in gfw.world.cleartime:
        total += gfw.world.cleartime[i]

def update():
    global ntime
    ntime = time.time() - stime


def draw():
    for b in gfw.world.objects_at(gfw.layer.bg):
        b.draw()

    for p in gfw.world.objects_at(gfw.layer.player):
        p.draw()

    for t in gfw.world.objects_at(gfw.layer.platform):
        t.draw()

    global image
    image.draw(get_canvas_width() // 2, get_canvas_height() // 2, get_canvas_width(), get_canvas_height())

    global font
    clr = "GAME CLEAR!!"
    font.draw(get_canvas_width() // 2 - 110, get_canvas_height() // 2 + 30, clr)

    global ntime

    if ntime > 1.5:
        minute = total // 60
        sec = total - minute * 60

        font.draw(get_canvas_width() // 2 - 200, get_canvas_height() // 2 - 20,
                  "Total Clear time: " + str(int(minute)).zfill(2) + ":" + str(int(sec)).zfill(2))

    if ntime > 3.5:
        font.draw(get_canvas_width() // 2 - 130, get_canvas_height() // 2 - 50,
                  "Press Any key")


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()

    global ntime
    if int(ntime) > 2.5 and e.type == SDL_KEYDOWN:
        for i in range(5):
            gfw.world.clear_at(i)
        gfw.pop()

    else:
        pass


def exit():
    global ending
    del ending