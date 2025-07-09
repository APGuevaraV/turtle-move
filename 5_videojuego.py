import turtle
import sys


window = turtle.Screen()
window.title("Aproximación a los videojuegos")
window.bgcolor("#eaefd7")
window.setup(500, 500)


class Tortuga(turtle.Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pensize(2)
        self.shape('turtle')
        self.color('darkgreen')

    def adelante(self):
        self.forward(10)

    def atras(self):
        self.backward(10)

    def izquierda(self):
        self.left(15)

    def derecha(self):
        self.right(15)


fio = Tortuga()

window.onkey(fio.adelante, 'w')
window.onkey(fio.atras, 's')
window.onkey(fio.izquierda, 'a')
window.onkey(fio.derecha, 'd')
window.onkey(sys.exit, 'e')
window.listen()
turtle.mainloop()
