import turtle

s=turtle.Screen()
t = turtle.Turtle()
t.shape()
t.begin_fill() #Inicia rellenado (negro es el colo predeterminado) todo el código que esté entre begin y end será el que estará rellenado
t.circle(100)
t.end_fill()#Termina el relleno

t.begin_fill()
t.color('white', 'white')
t.circle(45)
t.end_fill()

t.shape()#Establece la forma de nuestro marcador
"""
-Estas son las posibles formas que puede dar shape-

-turtle-Es tortuga
-arrow- Es una flecha media alargada
-square- Es un cuadrado
-triangle- Es un triangulo
-classic- Es la flecha que viene por default

"""
t.penup()#Levanta el lapiz y deja de dibujar , si hacemos algo más dejará de estar la línea pero el puntero se mostrará basanodose en los datos proporcianados
t.forward(100)
t.pendown()#Este muestra el lapiz(linea)
t.forward(50)
t.undo()#La tortuga deja de hacer la última acción, es decir se regresa; como un ctrl-z
t.clear()#Se limpia toda la pantalla pero la tortuga se quedará en el último lugar donde estuvo.
t.reset()#El programa se reinicia por completo.
t.forward(50)
t.stamp()#Se duplica el punero. EJEMPLO:Como en este caso se usó el forward de 50, justo en el 50 dejará su marca de agua(se duplica el puntero) y continúa el puntero hacia adelante.

turtle.done()

