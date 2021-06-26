from turtle import Turtle, Screen
from random import choice
# from turtle import *

juan = Turtle()
#juan.shape("turtle")
COLORES = ["red", "black", "green", "blue", "brown", "pink"]

# for _ in range(4):
#     juan.forward(100)
#     juan.right(90)

# # Ej 1
# for x in range (25):
#     juan.pd() if not x % 2 else juan.pu()
#     juan.forward(10)

# # Ej 2
# def poligono(num):
#     juan.color(choice(COLORES))
#     angulo = 360 / num
#     for _ in range(num):
#         juan.right(angulo)
#         juan.forward(100)

# for x in range(3, 11):
#     poligono(x)

# Ej 3
DIRECCIONES = [0,90,180,270]
juan.pensize(15)
juan.speed("fastest")
for _ in range(200):
    juan.color(choice(COLORES))
    juan.forward(30)
    juan.setheading(choice(DIRECCIONES))


pantalla = Screen()
pantalla.exitonclick()
