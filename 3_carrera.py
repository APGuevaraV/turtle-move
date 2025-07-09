import tkinter.messagebox
import turtle
import random
import tkinter

# personalizacion ventana
window = turtle.Screen()
window.title("Turtle runner")
window.bgcolor("#eaefd7")
window.setup(600, 400)
window.setworldcoordinates(0, 400, 600, 0)

tortugas = []

colores = ["yellow", "orange", "red", "brown", "purple",
           "blue", "cyan", "green", "black", "white"]

for i, color in enumerate(colores):
    tortuga = turtle.Turtle()
    tortuga.shape("turtle")
    tortuga.color(color)
    tortuga.pensize(2)
    tortuga.speed(4)
    tortuga.penup()
    tortuga.goto(10, i*40+15)
    tortuga.pendown()
    tortugas.append(tortuga)

run = True
while run:
    for tortuga in tortugas:
        distancia = random.randint(0, 25)
        tortuga.forward(distancia)
        if tortuga.xcor() > 560:
            tkinter.messagebox.showinfo(
                title="Fin de la carrera",
                message=f'Ganó la tortuga {tortuga.color()[0].capitalize()}'
            )
            run = False
            break

turtle.mainloop()
