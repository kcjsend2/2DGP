import random
from pico2d import *
import gfw
import gobj

canvas_width = 1280
canvas_height = 960

def enter():

def update():

def draw():
    for p in gfw.world.objects_at(gfw.layer.player):
        p.draw()

    for t in gfw.world.objects_at(gfw.layer.platform):
        t.draw()

def handle_event(e):


def exit():