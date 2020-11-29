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

    global display
    display = 0

    global image
    image = gfw.image.load(gobj.RES_DIR + '/WhiteSpace.png')

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
    image.draw(get_canvas_width() // 2, get_canvas_height() // 2, 600, 150)

    global font
    clr = "STAGE CLEAR!!"
    font.draw(get_canvas_width() // 2 - 110, get_canvas_height() // 2 + 30, clr)

    global ntime
    global display
    if display < now:
        display += 1

    if ntime > 2:
        minute = now // 60
        sec = now - minute * 60

        font.draw(get_canvas_width() // 2 - 155, get_canvas_height() // 2 - 30,
                  "Clear time: " + str(int(minute)).zfill(2) + ":" + str(int(sec)).zfill(2))

    if ntime > 2.5:
        font.draw(get_canvas_width() // 2 - 220, get_canvas_height() // 2 - 50,
                  "Press Any key to Continue")


def handle_event(e):
    global ntime
    if int(ntime) > 2.5:
        for i in range(5):
            gfw.world.clear_at(i)
        gfw.pop()

    else:
        pass


def exit():
    pass