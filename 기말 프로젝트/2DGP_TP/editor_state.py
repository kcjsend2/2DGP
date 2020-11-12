import random
from pico2d import *
import gfw
import gobj

canvas_width = 1280
canvas_height = 960

global horzSelected
horzSelected = 0

global VertSelected
VertSelected = 0

global CollisionMode
CollisionMode = False

def enter():
    gfw.world.init(['platform'])


def update():
    gfw.world.update()


def draw():
    gfw.world.draw()


def handle_event(e):
    global CollisionMode
    global horzSelected
    global VertSelected

    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        elif e.key == SDLK_1:
            CollisionMode = True
        elif e.key == SDLK_2:
            CollisionMode = False
        elif e.key == SDLK_LEFT and horzSelected > 0:
            horzSelected -= 1
        elif e.key == SDLK_RIGHT and horzSelected < 14:
            horzSelected += 1
        elif e.key == SDLK_UP and VertSelected > 0:
            horzSelected -= 1
        elif e.key == SDLK_DOWN and VertSelected < 10:
            horzSelected += 1


def exit():
    pass


if __name__ == '__main__':
    gfw.run_main()