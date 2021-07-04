# import tkinter module
from tkinter import *
from tkinter.ttk import *
# from random import *
    
# creating main tkinter window/toplevel
ventana = Tk()
  
# this wil create a label widget
l1 = Label(ventana, text = "First: ")
l2 = Label(ventana, text = "Second: ")
  
# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)
  
# entry widgets, used to take entry from user
e1 = Entry(ventana)
e2 = Entry(ventana)

# this will arrange entry widgets
e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)

def conversion(valor, unidad):
    pass

convertir = Button(text="Convertir", command=conversion)
convertir.grid(row = 2, column = 0, columnspan = 2, pady = 5)
# infinite loop which can be terminated by keyboard
# or mouse interrupt
mainloop()
