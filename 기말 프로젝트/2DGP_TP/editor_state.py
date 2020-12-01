import random
from pico2d import *
import gfw
import json
import gobj
from Tile import *
from item import *

canvas_width = 1280
canvas_height = 960

global xOffset
xOffset = 0
global yOffset
yOffset = 0

global horzSelected
horzSelected = 0

global VertSelected
VertSelected = 0

global CollisionMode
CollisionMode = False

global isFlag
isFlag = False

global isItem
isItem = False
global ItemType
ItemType = 0

global lDown
lDown = False

global rDown
rDown = False

global map
map = 'map_data/Stage7.json'
global item_map
item_map = 'map_data/Stage7_item.json'

def enter():
    global map
    gfw.world.init(['item', 'platform'])
    with open(map, 'r') as fp:
        data = json.load(fp)
        for d in data:
            t = Tile(d['x'], d['y'], d['sx'], d['sy'], d['isCollision'], d['isFlag'])
            gfw.world.add(gfw.layer.platform, t)
    with open(item_map, 'r') as fp:
        data = json.load(fp)
        for d in data:
            i = item(d['x'], d['y'], d['type'])
            gfw.world.add(gfw.layer.item, i)


def update():
    gfw.world.update()


def draw():
    global xOffset
    global yOffset
    for t in gfw.world.objects_at(gfw.layer.platform):
        t.image.clip_draw_to_origin(*t.sPos, t.width, t.height, t.pos[0] - xOffset, t.pos[1] - yOffset)

    image = gfw.image.load(gobj.RES_DIR + '/PrtWhite.png')
    image.clip_draw_to_origin(horzSelected * 32, VertSelected * 32, 32, 32, 0, canvas_height - 64, 64, 64)
    gobj.draw_collision_box(xOffset, yOffset)

    wimage = gfw.image.load(gobj.RES_DIR + '/Arms.png')
    for i in gfw.world.objects_at(gfw.layer.item):
        wimage.clip_draw_to_origin(i.type * 36, 0, 36, 13, i.pos[0] - xOffset, i.pos[1] - yOffset)



def handle_event(e):
    global CollisionMode
    global horzSelected
    global VertSelected
    global lDown
    global rDown
    global xOffset
    global yOffset
    global isFlag
    global isItem
    global ItemType

    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        elif e.key == SDLK_1:
            CollisionMode = True
            print("Collision: True")
        elif e.key == SDLK_2:
            CollisionMode = False
            print("Collision: False")
        elif e.key == SDLK_LEFT and horzSelected > 0:
            horzSelected -= 1
        elif e.key == SDLK_RIGHT and horzSelected < 15:
            horzSelected += 1
        elif e.key == SDLK_UP and VertSelected < 9:
            VertSelected += 1
        elif e.key == SDLK_DOWN and VertSelected > 0:
            VertSelected -= 1
        elif e.key == SDLK_p:
            save_tile()
        elif e.key == SDLK_f:
            if isFlag:
                isFlag = False
                print("Flag: False")
            else:
                isFlag = True
                print("Flag: True")

        elif e.key == SDLK_i:
            if isItem:
                isItem = False
                print("Item: False")
            else:
                isItem = True
                print("Item: True")

        elif e.key == SDLK_w:
            yOffset = yOffset + 32
        elif e.key == SDLK_a:
            if xOffset > 0:
                xOffset = xOffset - 32
        elif e.key == SDLK_s:
            if yOffset > 0:
                yOffset = yOffset - 32
        elif e.key == SDLK_d:
            xOffset = xOffset + 32

        elif e.key == SDLK_n:
            ItemType = 0
            print("ItemType: Gauss")
        elif e.key == SDLK_m:
            ItemType = 1
            print("ItemType: RocketLauncher")

    elif e.type == SDL_MOUSEBUTTONDOWN:
        if e.button == SDL_BUTTON_LEFT:
            lDown = True
            if not isItem:
                set_tile(e)
            else:
                set_item(e)
        if e.button == SDL_BUTTON_RIGHT:
            rDown = True
            if not isItem:
                del_tile(e)
            else:
                del_item(e)

    elif e.type == SDL_MOUSEBUTTONUP:
        if e.button == SDL_BUTTON_LEFT:
            lDown = False
        if e.button == SDL_BUTTON_RIGHT:
            rDown = False

    elif e.type == SDL_MOUSEMOTION:
        if lDown and not isItem:
            set_tile(e)
        elif rDown and not isItem:
            del_tile(e)


def exit():
    pass


def set_tile(e):
    global xOffset
    global yOffset

    mx = 0
    my = 0
    p2y = get_canvas_height() - e.y

    ibreak = False

    for i in range(40):
        for j in range(30):
            if i * 32 <= e.x < (i + 1) * 32 and j * 32 <= p2y < (j + 1) * 32:
                mx = i
                my = j
                ibreak = True
                break
        if ibreak:
            break

    isFill = False
    for p in gfw.world.objects_at(gfw.layer.platform):
        if p.tpos == [mx + xOffset / 32, my + yOffset / 32]:
            isFill = True

    if not isFill:
        t = Tile(mx * 32 + xOffset, my * 32 + yOffset, horzSelected * 32, VertSelected * 32, CollisionMode, isFlag)
        gfw.world.add(gfw.layer.platform, t)

def set_item(e):
    global xOffset
    global yOffset
    global ItemType

    p2y = get_canvas_height() - e.y

    t = item(e.x + xOffset, p2y + yOffset, ItemType)
    gfw.world.add(gfw.layer.item, t)


def del_tile(e):
    global xOffset
    global yOffset

    mx = 0
    my = 0
    p2y = get_canvas_height() - e.y

    ibreak = False

    for i in range(40):
        for j in range(30):
            if i * 32 <= e.x < (i + 1) * 32 and j * 32 <= p2y < (j + 1) * 32:
                mx = i
                my = j
                ibreak = True
                break
        if ibreak:
            break

    isFill = False
    for p in gfw.world.objects_at(gfw.layer.platform):
        if p.tpos == [mx + xOffset / 32, my + yOffset / 32]:
            print(p.tpos)
            target = p
            isFill = True

    if isFill:
        target.remove()

def del_item(e):
    global xOffset
    global yOffset

    p2y = get_canvas_height() - e.y

    target = None
    for i in gfw.world.objects_at(gfw.layer.item):
        if i.pos[0] - 18 <= e.x < i.pos[0] + 18 and i.pos[1] - 7 <= p2y < i.pos[1] + 7:
            target = i

    if target is not None:
        target.remove()

def save_tile():
    global map
    tile = gfw.world.objects_at(gfw.layer.platform)
    js_tiles = [t.dictionary() for t in tile]

    with open(map, 'w') as f:
        json.dump(js_tiles, f, indent=2)

    global item_map
    item = gfw.world.objects_at(gfw.layer.item)
    js_items = [i.dictionary() for i in item]

    with open(item_map, 'w') as f:
        json.dump(js_items, f, indent=2)

    print("File Saved!")


if __name__ == '__main__':
    gfw.run_main()