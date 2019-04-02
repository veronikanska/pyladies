from turtle import forward, left, right, clone, exitonclick, Turtle, xcor, ycor, goto, setheading, pensize

vetev = 100
setheading(90)

for x in range(10):
    pensize(x)
    forward(20 + 2 * x)
    left(45)

exitonclick()