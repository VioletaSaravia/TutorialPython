import colorgram
from turtle import Turtle, Screen
from random import choice

class ExtractorRGB():
    """Extrae los colores rgb en una lista de tuplas."""
    def __init__(self, imagen, cantidad):
        self.colores = colorgram.extract(imagen, cantidad)
        self.rgb = []
        for color in self.colores:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b
            nuevo_color = (r, b, g)
            self.rgb.append(nuevo_color)

    def limpiar(self):
        """Remueve blancos y negros."""
        limpio = [color for color in self.rgb if sum(color) < 600 and sum(color) > 30]
        self.rgb = limpio
        # for color in self.rgb:
        #     breakpoint()
        #     if sum(color) >= 600 or sum(color) < 30:
        #         self.rgb.remove(color)

class DibujarSpots():
    def __init__(self, pantalla, ref, matriz_x, matriz_y):
        self.dibujo = Turtle()
        self.dibujo.pu()
        self.dibujo.speed("fastest")
        self.dibujo.hideturtle()

        self.referencia = ExtractorRGB(ref, 20)
        self.referencia.limpiar()

        self.ratio_x = pantalla.window_width() / matriz_x
        self.ratio_y = pantalla.window_height() / matriz_y
        self.pos_x = self.ratio_x / 2
        self.pos_y = self.ratio_y / 2

        for x in range(matriz_x):
            for y in range(matriz_y):
                self.dibujo.goto(self.pos_x - 250, self.pos_y - 250)
                self.dibujo.dot(50, choice(self.referencia.rgb))
                self.pos_y += self.ratio_y
            self.pos_x += self.ratio_x
            self.pos_y = self.ratio_y / 2

                
pantalla = Screen()
pantalla.colormode(255)         # ???
pantalla.setup(500, 500)

referencia = input("Ingrese archivo de referencia: ")
mx = int(input("Cantidad X de circulos: "))
my = int(input("Cantidad Y de circulos: "))
spots = DibujarSpots(pantalla, referencia, mx, my)

# spots = ExtractorRGB('basico/spots.jpg', 20)
# spots.limpiar()


# nuevo_spots = Turtle()
# nuevo_spots.pu()
# pantalla.setup(500, 500)
# nuevo_spots.speed("fastest")
# nuevo_spots.hideturtle()

# matriz_x = 5
# matriz_y = 5
# ratio_x = (pantalla.window_width() / matriz_x)
# pos_x = ratio_x / 2
# ratio_y = (pantalla.window_height() / matriz_y)
# pos_y = ratio_y / 2
           
# for x in range(matriz_x):
#     for y in range(matriz_y):
#         nuevo_spots.goto(pos_x - 250, pos_y - 250)
#         nuevo_spots.dot(50, choice(spots.rgb))
#         pos_y += ratio_y
#     pos_x += ratio_x
#     pos_y = ratio_y / 2

pantalla.exitonclick()

