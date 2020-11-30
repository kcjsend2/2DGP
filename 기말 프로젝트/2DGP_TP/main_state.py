import gfw
from pico2d import *
from player import Player
from background import *
from Tile import *
from timer import *
import result_state
import gobj
import time
import pickle


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

global isPaused
isPaused = False

global pauseMenu
pauseMenu = 0

global timer

def enter():
    gfw.world.init(['bg', 'effect', 'platform', 'bullet', 'player', 'ui'])

    global t_max_x
    t_max_x = 0
    global t_max_y
    t_max_y = 0

    global isPaused
    isPaused = False

    global stage
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

    global bgm
    bgm = load_music('sound/bgm_' + str(random.randint(1, 3)) + '.ogg')
    bgm.set_volume(50)
    bgm.repeat_play()

def update():
    global isPaused
    global stage
    global timer
    if isPaused:
        return

    gfw.world.update()
    if player.get_goal():
        gfw.world.cleartime_add(stage, timer.get_time())
        gfw.push(result_state)

def draw():
    gfw.world.draw()
    if isPaused:
        global whitesp
        whitesp = gfw.load_image(gobj.RES_DIR + '/WhiteSpace.png')
        whitesp.draw(get_canvas_width() // 2, get_canvas_height() // 2 - 100, 400, 200)

        global pauseMenu
        global font
        pointer = ''
        if pauseMenu == 0:
            pointer = '->'
        font.draw(get_canvas_width() // 2 - 100, get_canvas_height() // 2 - 60, pointer + 'CONTINUE')

        pointer = ''
        if pauseMenu == 1:
            pointer = '->'
        font.draw(get_canvas_width() // 2 - 100, get_canvas_height() // 2 - 90, pointer + 'SAVE')

        pointer = ''
        if pauseMenu == 2:
            pointer = '->'
        font.draw(get_canvas_width() // 2 - 100, get_canvas_height() // 2 - 120, pointer + 'EXIT')


def handle_event(e):
    global player
    global TileSetMode
    global isPaused
    global pauseMenu

    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            pause_state()

    if not isPaused:
        player.handle_event(e)
    else:
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_DOWN and pauseMenu < 2:
                pauseMenu += 1
            elif e.key == SDLK_UP and pauseMenu > 0:
                pauseMenu -= 1
            elif e.key == SDLK_RETURN:
                if pauseMenu == 0:
                    isPaused = False
                elif pauseMenu == 1:
                    save_pickle()
                elif pauseMenu == 2:
                    gfw.pop()


def resume():
    global stage
    stage += 1
    enter()


def pause():
    pass


def pause_state():
    global isPaused
    if isPaused:
        isPaused = False
        for u in gfw.world.objects_at(gfw.layer.ui):
            if hasattr(u, 'isPaused'):
                u.isPaused = False
                u.stime += time.time() - u.paused
    else:
        isPaused = True
        for u in gfw.world.objects_at(gfw.layer.ui):
            if hasattr(u, 'isPaused'):
                u.isPaused = True
                u.paused = time.time()


def save_pickle():
    global stage
    with open('save.pickle', 'wb') as f:
        data = {"stage": stage, "cleartime": gfw.world.cleartime}
        pickle.dump(data, f)

def exit():
    global bgm
    del bgm


if __name__ == '__main__':
    gfw.run_main()
