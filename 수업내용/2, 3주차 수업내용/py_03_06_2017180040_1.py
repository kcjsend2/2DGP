from pico2d import *
from helper import *
import random


def handle_events():
    global running
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False

        if e.key == SDLK_ESCAPE:
            running = False

        elif e.type == SDL_MOUSEBUTTONDOWN:
            boy.speed += 1
            boy.list.append((e.x, get_canvas_height() - e.y - 1))
            boy.num += 1
            if boy.target is None:
                boy.target = boy.list[0]
                boy.delta = delta(boy.pos, (boy.list[0][0], boy.list[0][1]), boy.speed)
            elif boy.target:
                boy.delta = delta(boy.pos, (boy.list[0][0], boy.list[0][1]), boy.speed)


class Boy:
    def __init__(self):
        self.pos = (get_canvas_width() // 2, 80)

        self.image = load_image('../res/run_animation.png')

        self.delta = (0, 0)
        self.target = None

        self.speed = 0

        self.num = 0
        self.fidx = random.randint(0, 7)
        self.list = []

    def draw(self):
        self.image.clip_draw(self.fidx * 100, 0, 100, 100, self.pos[0], self.pos[1])

    def update(self):
        self.fidx = (self.fidx + 1) % 8


open_canvas()

boy = Boy()

running = True

while running:
    clear_canvas()

    boy.draw()
    update_canvas()

    handle_events()

    if boy.target:
        move_toward_obj(boy)
        boy.update()

    elif boy.num > 1:
        boy.num -= 1
        del boy.list[0]
        boy.target = boy.list[0]
        boy.target = boy.list[0]
        boy.delta = delta(boy.pos, (boy.list[0][0], boy.list[0][1]), boy.speed)
    elif boy.num == 1:
        boy.num -= 1
        del boy.list[0]
        boy.target = None
        boy.speed = 0

    delay(0.01)

close_canvas()