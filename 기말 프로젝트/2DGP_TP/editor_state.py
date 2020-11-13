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

global lDown
lDown = False

global rDown
rDown = False

def enter():
    gfw.world.init(['platform'])
    with open('MapData.json', 'r') as fp:
        data = json.load(fp)
        for d in data:
            t = Tile(d['x'], d['y'], d['sx'], d['sy'], d['isCollision'])
            gfw.world.add(gfw.layer.platform, t)


def update():
    gfw.world.update()


def draw():
    gfw.world.draw()
    image = gfw.image.load(gobj.RES_DIR + '/PrtWhite.png')
    image.clip_draw_to_origin(horzSelected * 32, VertSelected * 32, 32, 32, 0, canvas_height - 64, 64, 64)


def handle_event(e):
    global CollisionMode
    global horzSelected
    global VertSelected
    global lDown
    global rDown

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
        elif e.key == SDLK_UP and VertSelected < 9:
            VertSelected += 1
        elif e.key == SDLK_DOWN and VertSelected > 0:
            VertSelected -= 1
        elif e.key == SDLK_s:
            save_tile()
    elif e.type == SDL_MOUSEBUTTONDOWN:
        if e.button == SDL_BUTTON_LEFT:
            lDown = True
            set_tile(e)
        if e.button == SDL_BUTTON_RIGHT:
            rDown = True
            del_tile(e)

    elif e.type == SDL_MOUSEBUTTONUP:
        if e.button == SDL_BUTTON_LEFT:
            lDown = False
        if e.button == SDL_BUTTON_RIGHT:
            rDown = False

    elif e.type == SDL_MOUSEMOTION:
        if lDown:
            set_tile(e)
        elif rDown:
            del_tile(e)


def exit():
    pass


def set_tile(e):
    mx = 0
    my = 0
    p2y = get_canvas_height() - e.y

    ibreak = False

    for i in range(40):
        for j in range(30):
            if i * 32 < e.x < (i + 1) * 32 and j * 32 < p2y < (j + 1) * 32:
                mx = i
                my = j
                ibreak = True
                break
        if ibreak:
            break

    isFill = False
    for p in gfw.world.objects_at(gfw.layer.platform):
        if p.tpos == [mx, my]:
            isFill = True

    if not isFill:
        t = Tile(mx * 32, my * 32, horzSelected * 32, VertSelected * 32, CollisionMode)
        gfw.world.add(gfw.layer.platform, t)


def del_tile(e):
    mx = 0
    my = 0
    p2y = get_canvas_height() - e.y

    ibreak = False

    for i in range(40):
        for j in range(30):
            if i * 32 < e.x < (i + 1) * 32 and j * 32 < p2y < (j + 1) * 32:
                mx = i
                my = j
                ibreak = True
                break
        if ibreak:
            break

    isFill = False
    for p in gfw.world.objects_at(gfw.layer.platform):
        if p.tpos == [mx, my]:
            target = p
            isFill = True

    if isFill:
        target.remove()

def save_tile():
    tile = gfw.world.objects_at(gfw.layer.platform)
    js_tiles = [t.dictionary() for t in tile]

    with open('MapData.json', 'w') as f:
        json.dump(js_tiles, f, indent=2)


if __name__ == '__main__':
    gfw.run_main()