import turtle

def movepos(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

movepos(-400, 0)

turtle.forward(100)
turtle.setheading(-135)
turtle.forward(110)

turtle.setheading(45)
turtle.forward(50)
turtle.setheading(-45)
turtle.forward(60)

movepos(-250, 10)

turtle.setheading(-90)
turtle.forward(110)
turtle.setheading(90)
turtle.forward(60)
turtle.setheading(180)
turtle.forward(50)

movepos(-300, -100)

turtle.circle(40)

movepos(-100, 0)

turtle.setheading(-90)
turtle.forward(25)
turtle.setheading(180)
turtle.forward(50)
turtle.setheading(360)
turtle.forward(100)

movepos(-100, -100)

turtle.circle(30)

movepos(-25, 0)

turtle.setheading(-90)
turtle.forward(110)
turtle.setheading(90)
turtle.forward(60)
turtle.setheading(360)
turtle.forward(50)

movepos(-75, -120)

turtle.setheading(-90)
turtle.forward(25)
turtle.setheading(360)
turtle.forward(75)

movepos(100, 0)

turtle.setheading(-125)
turtle.forward(100)
turtle.setheading(55)
turtle.forward(80)
turtle.setheading(-55)
turtle.forward(80)

turtle.penup()
turtle.setheading(180)
turtle.forward(50)

turtle.pendown()
turtle.setheading(-90)
turtle.forward(25)
turtle.left(90)
turtle.forward(50)
turtle.right(180)
turtle.forward(100)

turtle.penup()
turtle.left(90)
turtle.forward(30)
turtle.left(90)

turtle.forward(10)
turtle.pendown()
turtle.forward(80)

turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(80)

turtle.left(90)
turtle.forward(15)
turtle.left(90)
turtle.forward(80)

turtle.exitonclick()

