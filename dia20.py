from turtle import Turtle, Screen
import time

pantalla = Screen()
pantalla.setup(600, 600)
pantalla.bgcolor("black")
pantalla.title("Snake v1.0")
pantalla.tracer(0)

class Miembro(Turtle):
    def __init__(self):
        Turtle.__init__(self)   # super() da error
        self.miembro = Turtle()
        self.miembro.shape('square')
        self.miembro.color('white')
        self.miembro.pu()
        self.miembro.speed('fastest')

    def ubicar_x(self, pos):
        return 0 if pos == 0 else self.miembro.goto(int(serpiente[0].xcor() - pos * 20), 0)

    def cont(self):
        self.miembro.forward(20)
                                                    
    def f(self):
        self.miembro.seth(90)
        self.miembro.forward(20)

    def l(self):
        self.miembro.seth(180)
        self.miembro.forward(20)

    def r(self):
        self.miembro.seth(0)
        self.miembro.forward(20)

    def d(self):
        self.miembro.seth(270)
        self.miembro.forward(20)

    def heading(self):
        return self.miembro.heading()

    def xcor(self):
        return self.miembro.xcor()

    def goto(self, xy):
        return self.miembro.goto(xy)

    def pos(self):
        return self.miembro.pos()
        

serpiente = [Miembro()]
largo = 6

for n in range(largo):
    serpiente.append(Miembro())
    serpiente[n+1].ubicar_x(n+1)

pantalla.update()
teclas = {                      # Sí, esto es un desastre
    'w' : (lambda: [seguir(), serpiente[0].f(), pantalla.update()] if serpiente[0].heading() != 90 and serpiente[0].heading() != 270 else 0),
    'a' : (lambda: [seguir(), serpiente[0].l(), pantalla.update()] if serpiente[0].heading() != 180 and serpiente[0].heading() != 0 else 0),
    'd' : (lambda: [seguir(), serpiente[0].r(), pantalla.update()] if serpiente[0].heading() != 0 and serpiente[0].heading() != 180 else 0),
    's' : (lambda: [seguir(), serpiente[0].d(), pantalla.update()] if serpiente[0].heading() != 270 and serpiente[0].heading() != 90 else 0),
}

def seguir():
    #breakpoint()
    for n in range(len(serpiente)-1, 0, -1):
        serpiente[n].goto(serpiente[n-1].pos())

pantalla.listen()

def avanzar():
    seguir()
    serpiente[0].f()
    pantalla.update()

for tecla, accion in teclas.items(): # condicional para no girar y avanzar a la vez
    pantalla.onkey(key=tecla, fun=accion)

while True:
    seguir()
    serpiente[0].cont()
    pantalla.update()
    time.sleep(0.3)


pantalla.exitonclick()
