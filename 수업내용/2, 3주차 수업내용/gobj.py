from pico2d import*
import random


class Boy:
    def __init__(self):
        self.x, self.y = get_canvas_width() // 2, 80
        self.image = load_image('../res/run_animation.png')
        self.x = random.randint(100, 700)
        self.y = random.randint(100, 500)
        self.dx = random.random()
        self.fidx = random.randint(0, 7)

    def draw(self):
        self.image.clip_draw(self.fidx * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.fidx = (self.fidx + 1) % 8
        self.x += self.dx * 5


class Grass:
    def __init__(self):
        self.image = load_image('../res/grass.png')
        self.x, self.y = 400, 30

    def draw(self):
        self.image.draw(self.x, self.y)


if __name__ == '__main__':
    print("Not imported")