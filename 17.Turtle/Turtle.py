import turtle
'''Es un modulo de programación grafica de python, que se basa en coordenaddas relativas del plano cartesiano.'''

s = turtle.Screen()#Muestra el recuadro de pantalla 
t = turtle.Turtle()#Establecemos la variable igualada a la libreria que se importó.

t.goto(100,100)#Manda el lapicero a un punto en especifico de nuestra pantalla por medio de cordenadas(basandose en un plano cartesiono)
t.home() #Manda al puntero de forma directa al punto 0.0 (cordenadas del plano cartesiano)
t.speed(10)
t.circle(10)

t.dot(30)#Establece el valor del diametro(aplica en los circulos)
t.forward(100)#Adelante
t.right(90)#Avanza a la derecha
t.left(10)#Avanza a la izquierda
t.hideturtle() #La tortuga/puntero desaparece
t.speed(1)
t.circle(40)
t.showturtle()#Muestra la tortuga(puntero)
t.circle(100)

t.sety()




turtle.done()#Deja la pantalla(screen) abierta.

