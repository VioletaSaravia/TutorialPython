from turtle import Turtle, Screen
import time
import random

pantalla = None
def set_pantalla():             # Class!
    global pantalla
    if pantalla:
        pantalla.clearscreen()
    if not pantalla:
        pantalla = Screen()
    pantalla.setup(600, 600)
    pantalla.bgcolor("black")
    pantalla.title("Snake v0.1")
    pantalla.tracer(0)

set_pantalla()

class Comida(Turtle):
    def __init__(self):
        Turtle.__init__(self)   # super() también da error acá??¿¿?
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.place()

    def place(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

class Miembro(Turtle):
    def __init__(self):
        Turtle.__init__(self)  # super() da error
        super().shape('square')
        super().color('white')
        super().pu()
        super().speed('fastest')

    def forward(self, angle = 1):
        # el if no funciona :(
        if serpiente[0].heading() != angle and serpiente[0].heading != (angle + 180) % 360:
            if not angle == 1:
                super().seth(angle)
            #breakpoint()
            super().forward(20)
            seguir()
            pantalla.update()

serpiente = []
comida = None

def seguir():
    if len(serpiente) == 1:
        largo = 3
        for n in range(largo):
            serpiente.append(Miembro())
    for n in range(len(serpiente)-1, 0, -1):
        serpiente[n].goto(serpiente[n-1].pos())


def set_tablero():              # Class!
    global tablero
    tablero = Turtle()
    tablero.pu()
    tablero.color('white')
    tablero.ht()
    tablero.goto(-280, -280)

def setup():
    global serpiente
    serpiente = [Miembro()]
    global comida
    comida = Comida()
    set_tablero()

    
    seguir()
    pantalla.update()

teclas = {                     
    'w' : (lambda: serpiente[0].forward(90) if serpiente[0].heading() != 90 and serpiente[0].heading() != 270 else 0),
    'a' : (lambda: serpiente[0].forward(180) if serpiente[0].heading() != 180 and serpiente[0].heading() != 0 else 0),
    'd' : (lambda: serpiente[0].forward(0) if serpiente[0].heading() != 0 and serpiente[0].heading() != 180 else 0),
    's' : (lambda: serpiente[0].forward(270) if serpiente[0].heading() != 270 and serpiente[0].heading() != 90 else 0),
}

pantalla.listen()


sleeptime = 0.15


def restart():
    for miembro in serpiente:
        miembro.clear()
    comida.clear()
    set_pantalla()

with open('high_score.txt') as data:
    high_score = int(data.read())

def game(score = 0):
    global high_score
    for tecla, accion in teclas.items():
        # condicional para no girar y avanzar a la vez
        pantalla.onkey(key=tecla, fun=accion)
    serpiente[0].forward()
    if serpiente[0].distance(comida) < 15:
        comida.place()
        serpiente.append(Miembro())
        score += 1
        high_score = score if score > high_score else high_score
        with open('high_score.txt', 'w') as data:
            data.write(str(high_score))
    tablero.clear()
    tablero.write(f'Puntaje: {score} // Puntaje máximo: {high_score}')
        #sleeptime -= 0.01
    # Simplificar esto ->
    for miembro in serpiente[2:]:
        if serpiente[0].distance(miembro) <15:
            restart()
            setup()
            score = 0
    if serpiente[0].xcor() > 295 or serpiente[0].xcor() < -295:
        restart()
        setup()
        score = 0
    if serpiente[0].ycor() > 295 or serpiente[0].ycor() < -295:
        restart()
        setup()
        score = 0
    time.sleep(sleeptime)
    return game(score) # NO USAR RECURSION -.-

setup()
game()
pantalla.exitonclick()
