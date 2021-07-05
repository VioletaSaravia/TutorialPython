from tkinter import *
from tkinter.ttk import *
from random import choice
import string

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

CHARS = string.digits + string.punctuation + string.ascii_letters

def generate_password(size = 12, chars = CHARS):
    pass_gen = ''.join([choice(chars) for _ in range(size)])
    return password.insert(0, pass_gen)

# ---------------------------- SAVE PASSWORD ------------------------------- #

with open('log.txt') as log:
    DB = log.read()

def save_password():
    global DB
    DB = DB.join([web.get(), user.get(), password.get()]) # usar pandas
    with open('logo.txt', 'w') as log:
        log.write(DB)
        log.close()
    return

# ---------------------------- UI SETUP ------------------------------- #

TITULO = "Password Manager v0.1"

ventana = Tk()
ventana.title(TITULO)
ventana.config(padx = 20, pady = 20) #bg='white'
canvas = Canvas(width = 200, height = 200)
#canvas.pack()
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
