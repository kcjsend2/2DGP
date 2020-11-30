import random
from pico2d import *
import gfw
import gobj

canvas_width = 1280
canvas_height = 960

global font
global image


def enter():
    global font
    font = gfw.font.load(gobj.RES_DIR + 'ENCR10B.TTF', 30)
    global image
    image = gfw.image.load(gobj.RES_DIR + '/BlackSpace.png')


def update():
    pass


def draw():
    global image
    image.draw(get_canvas_width() // 2, get_canvas_height() // 2, 600, 150)

    global font
    font.draw(get_canvas_width() // 2 - 110, get_canvas_height() // 2 + 30, clr)


def handle_event(e):
    pass


def exit():
    pass
