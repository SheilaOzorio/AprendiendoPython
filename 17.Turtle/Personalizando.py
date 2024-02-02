import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor('gray') #Color de fondo de nuestra pantalla
s.title('Proyecto 1')

t.shapesize(3,3,3)#Tamaño de nuestra tortuga/marcador. Primer valor es ancho, 2do largo, y 3ro es el borde
t.fillcolor('Pink') #Establece el color de nuestro marcador

t.forward(100)
t.pencolor("red")#Establce el color de margen de nuestra tortuga/marcador y el color que será de las líneas que deje.
t.forward(150)

t.color('white')#Establece el color de la tortuga/marcador y de la tinta.
t.right(90)
t.forward(100)

t.pensize(5)#Establece el grosor de nuestra línea
t.forward(100) 

turtle.done()