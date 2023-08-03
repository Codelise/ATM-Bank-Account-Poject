import turtle

heart = turtle.Turtle()

heart.speed(2)

heart.begin_fill()
heart.fillcolor("red")
heart.left(140)
heart.forward(180)
heart.circle(-90, 200)

heart.left(120)
heart.circle(-90, 200)
heart.forward(180)
heart.end_fill()

heart.hideturtle()

turtle.done()