"""Dia 19 - Object state and instances"""

from turtle import Turtle, Screen
from random import choice
# from turtle import *

juan = Turtle()
pantalla = Screen()

teclas = {
    'w' : (lambda: juan.forward(10)),
    'a' : (lambda: juan.left(10)),
    's' : (lambda: juan.backwards(10)),
    'd' : (lambda: juan.right(10)),
    'c' : (lambda: [juan.clear(), juan.pu(), juan.home(), juan.pd()])
}

pantalla.listen()
for tecla, func in teclas.items():
    pantalla.onkey(key=tecla, fun=func)

pantalla.exitonclick()
