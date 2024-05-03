import turtle

turtle.title ("Virus")

a = 0
b = 0

turtle.bgcolor("black")
turtle.speed(0)
turtle.pencolor("pink")
turtle.penup()
turtle.goto(0,200)
turtle.pendown()

while True:
    turtle.forward(a)
    turtle.right(b)
    a += 4
    b += 1
    if b == 600:
        break

turtle.exitonclick()

