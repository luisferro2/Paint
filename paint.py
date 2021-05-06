from turtle import *
import turtle
from freegames import vector
import numpy as np
import math


def line(start, end):
    "Draw line from start to end."
    up() # Not drawing when moving.
    goto(start.x, start.y)
    down() # Drawing when moving.
    goto(end.x, end.y)


def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    "Draw circle from start to end."
    line(start, end)
    diameter = np.sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2)
    radius = diameter / 2
    center = [start.x + (end.x - start.x) / 2, start.y + (end.y - start.y) / 2]
    bottom = [center[0]] + [center[1] - radius]
    up()
    goto(bottom[0], bottom[1])
    down()
    turtle.circle(radius)


def rectangle(start, end):
    "Draws a rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    
    begin_fill()
    forward(end.x - start.x)
    left(90)
    forward(end.y - start.y)
    left(90)
    forward(end.x - start.x)
    left(90)
    forward(end.y - start.y)
    left(90)
    end_fill()


def triangle(start, end):
    "Draws a right angled scalene triangle from start to end"
    up()
    goto(start.x, start.y)
    down()
    
    hip = math.sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2)
    alpha = math.acos((end.x - start.x) / hip) * 180 / math.pi
    
    begin_fill()
    forward(end.x - start.x)
    left(90)
    forward(end.y - start.y)
    left(90 + alpha)
    forward(hip)
    left(180 - alpha)
    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
