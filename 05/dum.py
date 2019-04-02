from turtle import forward, left, right, exitonclick
from math import atan, degrees, sqrt

vyska = int(input('Zadej vysku domu: '))
sirka = int(input('Zadej sirku domu: '))

def dum(a, b):
    'Nakresli dum'
    u = sqrt(a**2 + b**2)
    alfa = degrees(atan(b / a))
    delta = 180 - 2*alfa
    for _ in range(2):
        forward(a)
        left(90)
        forward(b)
        left(90)
    left(alfa)
    forward(u)
    left(delta)
    forward(u / 2)
    left(180 - delta)
    forward(u / 2)
    left(delta)
    forward(u)
    return True

dum(vyska, sirka)
exitonclick()