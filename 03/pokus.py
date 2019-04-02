from turtle import forward, left, exitonclick, goto, setheading, penup, pendown
from math import sqrt


smer = 140
strana = smer - 90
vrchol = strana / sqrt(3)
u = 0

setheading(210)
penup()

for smer in range(0,360):
    if smer > 360:
        u = smer - 360
    else:
        u == smer
    left(u + 3)
    forward(vrchol)
    left(150)
    pendown()
    for _ in range(3):
        forward(strana)
        left(120)
    penup()    
    goto(0,0)


exitonclick()