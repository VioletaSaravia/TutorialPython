from tkinter import *
from tkinter.ttk import *
from random import choice
import string
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

CHARS = string.digits + string.punctuation + string.ascii_letters

def generate_password(size = 12, chars = CHARS):
    pass_gen = ''.join([choice(chars) for _ in range(size)]) # .join('\n')
    password.delete(0, END)
    password.insert(0, pass_gen)

# ------------------------------ SAVE PASSWORD ---------------------------------- #

def save_password():
    DB = { 'Web' : web.get(),
           'Username' : user.get(),
           'Password' : password.get()
          }  # usar pandas
    try:
        with open('log.json', 'a') as log:
            log.write(json.dumps(DB))
    except FileNotFoundError as filenotfound:
        create_yes = input(f'{filenotfound} doesn\'t exist. Create? [y/n] ')
        if create_yes == 'y':
            with open('log.json', 'w') as log:
                log.write(json.dumps(DB)) # !!! load(), update() y dump ()
                                          # en vez de dump
                #json.dumps(DB, log)
    # web.delete(0, END)
    # user.delete(0, END)
    # password.delete(0, END)
    fields = ['web', 'user', 'password']
    for field in fields:
        exec(f'{field}.delete(0, END)')
    return
# ---------------------------------- LOOKUP ------------------------------------- #

def lookup():
    database = json.load('log.json')
    breakpoint()

# --------------------------------- UI SETUP ------------------------------------ #

TITULO = "Password Manager v0.1"

ventana = Tk()
ventana.title(TITULO)
ventana.config(padx = 20, pady = 20) #bg='white'

canvas = Canvas(width = 200, height = 200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=0, row=0, columnspan=4)

web_label = Label(text="Website: ")
web_label.grid(column=0, row=1)
web = Entry(ventana)
web.grid(column=1, row=1, padx=5, pady=5, columnspan=2, sticky="nsew")
web.focus()

user_label = Label(text="Username/Email: ")
user_label.grid(column=0, row=2)
user = Entry(ventana)
user.insert(0, "saraviavioleta@gmail.com")
user.grid(column=1, row=2, padx=5, pady=5, columnspan=2, sticky="nsew")

pass_label = Label(text="Password: ") # usar nombre de la variable como txt?
pass_label.grid(column=0, row=3)
password = Entry(ventana)
password.grid(column=1, row=3, padx=5, pady=5)

generator = Button(text="Generate Password", width=16, command=generate_password)
generator.grid(column=2, row=3, padx=5, pady=5) # class out pads

add = Button(text="Add", command=save_password)
add.grid(column=1, row=4, columnspan=3, padx=5, pady=5)
mainloop()
