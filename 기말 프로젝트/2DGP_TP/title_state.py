import random
from pico2d import *
import gfw
import gobj
import time
import main_state
import pickle

canvas_width = 1280
canvas_height = 960

global font
global image
global menu_select


def enter():
    global introtime
    introtime = 0

    global font
    font = gfw.font.load(gobj.RES_DIR + 'ENCR10B.TTF', 30)

    global bg
    bg = gfw.image.load(gobj.RES_DIR + '/bkMoon.png')

    global title
    title = gfw.image.load(gobj.RES_DIR + '/title.png')

    global menu_select
    menu_select = 0

    global whitesp
    whitesp = gfw.image.load(gobj.RES_DIR + '/WhiteSpace.png')

    global intro
    intro = load_music('sound/curly_intro.ogg')
    intro.set_volume(50)
    intro.play()

    global loop
    loop = load_music('sound/curly_loop.ogg')
    loop.set_volume(50)

    global isloop
    isloop = False

def update():
    global introtime
    introtime += gfw.delta_time

    global intro
    global loop
    global isloop
    if introtime > 13.25 and not isloop:
        isloop = True
        intro.stop()
        loop.repeat_play()


def draw():
    global bg
    bg.draw_to_origin(0, 0, get_canvas_width(), get_canvas_height())

    global title
    title.draw(get_canvas_width() // 2, get_canvas_height() // 2 + 100)

    global whitesp
    whitesp.draw(get_canvas_width() // 2, get_canvas_height() // 2 - 100, 400, 200)

    global font
    pointer = ''
    if menu_select == 0:
        pointer = '->'
    font.draw(get_canvas_width() // 2 - 100, get_canvas_height() // 2 - 60, pointer + 'START')

    pointer = ''
    if menu_select == 1:
        pointer = '->'
    font.draw(get_canvas_width() // 2 - 100, get_canvas_height() // 2 - 90, pointer + 'LOAD')

    pointer = ''
    if menu_select == 2:
        pointer = '->'
    font.draw(get_canvas_width() // 2 - 100, get_canvas_height() // 2 - 120, pointer + 'EXIT')



def load_pickle():
    with open('save.pickle', 'rb') as f:
        data = pickle.load(f)
        main_state.stage = data["stage"]
        gfw.world.cleartime = data["cleartime"]


def handle_event(e):
    global menu_select

    if e.type == SDL_QUIT:
        gfw.quit()
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_DOWN and menu_select < 2:
            menu_select += 1
        if e.key == SDLK_UP and menu_select > 0:
            menu_select -= 1
        if e.key == SDLK_RETURN:
            if menu_select == 0:
                gfw.world.cleartime.clear()
                main_state.stage = 1
                gfw.push(main_state)
            elif menu_select == 1:
                load_pickle()
                gfw.push(main_state)
            elif menu_select == 2:
                gfw.quit()


def exit():
    global intro
    global loop

    del intro
    del loop


def pause():
    pass

def resume():
    enter()

if __name__ == '__main__':
    gfw.run_main()