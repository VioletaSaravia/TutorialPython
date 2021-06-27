from turtle import Turtle, Screen
import random
from random import choice
# from turtle import *

COLORES = ["red", "black", "green", "blue", "brown", "pink", "black", "orange"]

def Inicio():
    #__INIT__
    sin_usar = COLORES
    cantidad = int(input("Cuántas tortugas van a correr? "))
    apuesta = input("A cual quiere apostar? ")

    #CREAR TORTUGAS
    tortugas = [Turtle() for i in range(cantidad)]
    tortugas[0].color(apuesta)
    sin_usar.remove(apuesta)
    for tortuga in tortugas[1:]:
        color = choice(sin_usar)
        sin_usar.remove(color)
        tortuga.color(color)

    #UBICAR TORTUGAS
    separacion = pantalla_y / cantidad
    ubicacion = separacion / 2 - pantalla_y / 2
    for tortuga in tortugas:
        tortuga.pu()
        tortuga.goto((pantalla_x / 10) - (pantalla_x / 2), ubicacion)
        ubicacion += separacion

    #DECIDIR GANADORA
    def ganadora():
        for tortuga in tortugas:
            if tortuga.xcor() == pantalla_x / 2:
                return tortuga.pencolor()
        return
            
    #CORRER CARRERA
    while True:
        color_ganadora = ganadora()
        if color_ganadora:
            break
        for tortuga in tortugas:
            tortuga.forward(random.randint(5, 15))

    print(f'Ganó {color_ganadora}.')
    
    return Inicio() if input("Jugar otra? (y/N) ") == 'y' else 0
        
pantalla_x = 1000
pantalla_y = 500
pantalla = Screen()
pantalla.setup(pantalla_x, pantalla_y)

Inicio()

pantalla.bye()
