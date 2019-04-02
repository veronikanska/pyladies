from turtle import forward, left, exitonclick
from math import sqrt

n = int(input('Kolik stran ma tvuj n-uhelnik? '))

strana = 500 / n
uhel = 360 / n

for _ in range(0, n):
    forward(strana)
    left(uhel)

exitonclick()