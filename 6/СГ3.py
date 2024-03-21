import turtle
from turtle import *

# Мгновенное рисование
turtle.tracer(0)
koef = 20

# Рисование фигуры
for i in range(4):
    for j in range(4):
        forward(7 * koef)
        right(90)
    forward(10 * koef)
    right(90)
    forward(4 * koef)

# Рисование сетки
up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(4)
done()
