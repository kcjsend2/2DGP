from pico2d import *


def handle_events():
    global running
    global d
    global x
    global y
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False

        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_RIGHT:
                d += 1
            elif e.key == SDLK_LEFT:
                d -= 1
            elif e.key == SDLK_ESCAPE:
                running = False

        elif e.type == SDL_KEYUP:
            if e.key == SDLK_RIGHT:
                d -= 1
            elif e.key == SDLK_LEFT:
                d += 1

        elif e.type == SDL_MOUSEMOTION:
            x, y = e.x, get_canvas_height() - e.y - 1


open_canvas()

grass = load_image('res/grass.png')
character = load_image('res/run_animation.png')

running = True
x, y = get_canvas_width() // 2, 80
frame = 0
d = 0

hide_cursor()

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += d * 5
    delay(0.03)

close_canvas()