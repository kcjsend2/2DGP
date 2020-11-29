import gfw
from pico2d import *
from player import Player
from background import *
from Tile import *
from timer import *
import result_state
import gobj
import time


canvas_width = 1280
canvas_height = 960

global xOffset
global yOffset

global t_max_x
global t_max_y
global player

global stime
global font

global stage
stage = 1

def enter():
    gfw.world.init(['bg', 'bullet', 'effect', 'platform', 'player', 'ui'])

    global t_max_x
    t_max_x = 0
    global t_max_y
    t_max_y = 0

    with open("Stage" + str(stage) + ".json", 'r') as fp:
        data = json.load(fp)
        for d in data:
            t = Tile(d['x'], d['y'], d['sx'], d['sy'], d['isCollision'], d['isFlag'])
            gfw.world.add(gfw.layer.platform, t)
            if t.pos[0] > t_max_x:
                t_max_x = t.pos[0]
            if t.pos[1] > t_max_y:
                t_max_y = t.pos[1]

    global player
    player = Player(t_max_x, t_max_y)
    gfw.world.add(gfw.layer.player, player)

    bg = Background('bkMoon.png', t_max_x, t_max_y)
    gfw.world.add(gfw.layer.bg, bg)

    global stime
    stime = time.time()

    global font
    font = gfw.font.load(res('ENCR10B.TTF'), 30)

    global timer
    timer = Timer(canvas_width - 20, canvas_height - 50)
    gfw.world.add(gfw.layer.ui, timer)

def update():
    gfw.world.update()
    if player.get_goal():
        gfw.push(result_state)

def draw():
    gfw.world.draw()


def handle_event(e):
    global player
    global TileSetMode

    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)

def resume():
    global stage
    stage += 1
    enter()

def pause():
    pass

def exit():
    pass


if __name__ == '__main__':
    gfw.run_main()
