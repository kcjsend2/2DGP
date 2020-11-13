import random
from pico2d import *
import gfw
import json
import gobj
from Tile import *

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
    with open('MapData.json', 'r') as fp:
        data = json.load(fp)
        for d in data:
            t = Tile(d.x, d.y, d.sx, d.sy, d.w, d.h, d.isCollision)
            gfw.world.add('platfrom', t)


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
            VertSelected -= 1
        elif e.key == SDLK_DOWN and VertSelected < 10:
            VertSelected += 1
        elif e.key == SDLK_s:
            save_Tile()
    elif e.type == SDL_MOUSEBUTTONDOWN:
        if e.key == SDL_BUTTON_LEFT:



def exit():
    pass

def save_Tile():
    tile = gfw.world.objects_at(gfw.layer.platform)
    js_tiles = [t.dictionary() for t in tile]

    with open('MapData.json', 'w') as f:
        json.dump(js_tiles, f, indent=2)


if __name__ == '__main__':
    gfw.run_main()