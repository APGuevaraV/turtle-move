import turtle

#personalizacion ventana
window = turtle.Screen()
window.title("Viaje con Fio")
window.bgcolor("#eaefd7")
window.setup(500,500)
window.setworldcoordinates(0,500,500,0)


#configuracion de la tortuga
fio = turtle.Turtle()
fio.shape('turtle')
fio.color('darkgreen')
fio.pensize(2)
fio.speed(2)


#instrucciones
fio.penup()
fio.goto(200,200)
fio.pendown()
fio.goto(350,200)
fio.goto(350,350)
fio.goto(200,350)
fio.goto(200,200)
print(fio.pos())

fio.circle(25)
fio.circle(50)
fio.circle(75)
fio.circle(150)

for i in range(0,5):
    fio.penup()
    fio.goto(i*25,i*25)
    fio.pendown()
    fio.circle(i*25)

turtle.mainloop()