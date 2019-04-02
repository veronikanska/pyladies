from turtle import forward, left, exitonclick
from math import sqrt

strana = 50
uhlopricka = sqrt(2) * strana

for _ in range(10):
    for _ in range(4):
        forward(strana)
        left(90)
    left(45)
    forward(uhlopricka)
    for _ in range(2):
        left(90)
        forward(uhlopricka / 2)
    left(90)
    forward(uhlopricka)
    left(45)
    forward(20)

exitonclick()


exitonclick()