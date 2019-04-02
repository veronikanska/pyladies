from turtle import forward, left, exitonclick, setheading, circle, goto

for _ in range(18):          # pokud se sprom2nnou nepracuje, d8v8 se tam podtrzitko (neco tam byt musi)
    for _ in range(4):
        forward(50)
        left(90)
    left (20)

setheading(270)
forward(80)
setheading(0)

for polomer in range(60, 180, 20):
    circle(polomer, 45)
    setheading(180)
    circle(polomer, 45)
    setheading(270)
    forward(50)
    setheading(0)

goto(0,-105)
setheading(150)

for polomer in range(60, 180, 20):
    circle(polomer, 45)
    setheading(-30)
    circle(polomer, 45)
    setheading(270)
    forward(50)
    setheading(150)

exitonclick()