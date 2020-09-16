import turtle

def movepos(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

for i in [0, 1, 2, 3, 4, 5]:
    movepos(i * 100, 500)
    turtle.goto(i * 100, 0)

for i in [0, 1, 2, 3, 4, 5]:
    movepos(0, i * 100)
    turtle.goto(500, i * 100)
