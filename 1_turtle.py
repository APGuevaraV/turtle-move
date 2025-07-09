import turtle

#personalizacion ventana
window = turtle.Screen()
window.title("Viaje con Fio")
window.bgcolor("#eaefd7")
window.setup(500,500)

#configuracion de la tortuga
fio = turtle.Turtle()
fio.shape('turtle')
fio.color('darkgreen')
fio.pensize(2)
fio.speed(1)


#instrucciones
fio.forward(100)
fio.left(90)
fio.forward(150)
fio.home()

turtle.mainloop()