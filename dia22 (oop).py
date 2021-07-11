from turtle import Turtle, Screen
import random
import time

class Objeto(Turtle):
    def __init__(self):
        Turtle.__init__(self)  # super() da error
        super().shape('square')
        super().color('white')
        super().speed('fastest')
        super().pu()

class Bola(Objeto):
    def __init__(self):
        Objeto.__init__(self)

    def inicio(self):
        self.goto(0, 0)
        self.seth(random.randint(1, 359)) # TODO: reducir rango
        # while True:
        #     self.forward(10)

    def rebotar(self, ang):
        if ang == 1:
            return self.seth((180 - self.heading()) % 360)
        if ang == 2:
            return self.seth((360 - self.heading()))

    def colision(self):
        global jugadores
        for objeto in jugadores:
            if self.distance(objeto) < 20:
                return self.rebotar(1)
        if self.ycor() > 290 or self.ycor() < -290: # TODO: resolución ajustable
            return self.rebotar(2)
        if self.xcor() > 290 or self.xcor() < -290:
            return self.inicio()

class Tablero(Objeto):
    def __init__(self):
        Objeto.__init__(self)
        self.ht()
        self.goto(-280, -280)
        # self.clear()
        # self.write(f'Puntaje: {score}')

class Jugador(Objeto):
    def __init__(self):
        Objeto.__init__(self)
        self.turtlesize(stretch_len = 5)
        self.seth(90)

    def subir(self):
        self.seth(90)
        self.forward(10)

    def bajar(self):
        self.seth(270)
        self.forward(30)

pantalla = Screen()
pantalla.setup(600, 600)
pantalla.bgcolor("black")
pantalla.title("Pong v0.1")
#pantalla.tracer(0)
jugadores = [Jugador(), Jugador()]
bola = Bola()

teclas = {
    'w' : (lambda: jugadores[0].subir()),
    's' : (lambda: jugadores[0].bajar()),
    'i' : (lambda: jugadores[1].subir()),
    'k' : (lambda: jugadores[1].bajar())
}

jugadores[0].goto(-260, 0)
jugadores[1].goto(260, 0)
time.sleep(1)
pantalla.listen()
bola.inicio()

while True:
    for tecla, accion in teclas.items():
        pantalla.onkey(key=tecla, fun=accion)
    bola.forward(4)
    bola.colision()
    #pantalla.update()


pantalla.exitonclick()
