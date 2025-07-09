import turtle
import math

#personalizacion ventana
window = turtle.Screen()
window.title("Viaje con Fio")
window.bgcolor("#eaefd7")
window.setup(500,500)
window.setworldcoordinates(0,500,500,0)

class Tortuga(turtle.Turtle):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.pensize(2)
        self.shape('turtle')
        self.color('darkgreen')

    def rectangulo(self,x,y,ancho,alto,color='black'):
        self.color(color)
        self.penup()
        self.goto(x-ancho/2, y-alto/2)
        self.pendown()
        self.goto(x+ancho/2, y-alto/2)
        self.goto(x+ancho/2, y+alto/2)
        self.goto(x-ancho/2, y+alto/2)
        self.goto(x-ancho/2, y-alto/2)
        
        
    def poligono(self,lados,radio,color="black"):
        self.color(color)
        angulo = math.pi * 2 /lados
        ancho_ventana = window.screensize()[0]/2
        alto_ventana = window.screensize()[1]/2
        x= radio * math.sin(angulo) + ancho_ventana
        y= radio * math.cos(angulo) + alto_ventana
        self.penup()
        self.goto(x,y)
        self.pendown()
        for i in range(lados +1):
            x= radio * math.sin(angulo * i) + ancho_ventana
            y= radio * math.cos(angulo * i) + alto_ventana
            self.goto(x,y)
        


        
fio = Tortuga()
x,y =(250,250)
w,h=(50,50)
inc = 50

"""X
for color in ["yellow","orange","red","brown","purple","blue","cyan","green","black"]:
    fio.rectangulo(x,y,w,h,color=color)
    w+= inc
    h+= inc
"""

for i in range(3,25):
    fio.poligono(i,i*10)

turtle.mainloop()
        
        
        
    