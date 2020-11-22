import gfw
from pico2d import *
from player import Player
from background import *
from Tile import *
import gobj

canvas_width = 1280
canvas_height = 960

def enter():
    gfw.world.init(['bg', 'bullet', 'effect', 'platform', 'player'])

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    bg = Background('bkMoon.png')
    gfw.world.add(gfw.layer.bg, bg)

    with open('MapData.json', 'r') as fp:
        data = json.load(fp)
        for d in data:
            t = Tile(d['x'], d['y'], d['sx'], d['sy'], d['isCollision'])
            gfw.world.add(gfw.layer.platform, t)


def update():
    gfw.world.update()


def draw():
    gfw.world.draw()
    gobj.draw_collision_box()


def handle_event(e):
    global player
    global TileSetMode

    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)


def exit():
    pass


if __name__ == '__main__':
    gfw.run_main()
