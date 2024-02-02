import turtle
s= turtle.Screen()
t = turtle.Turtle()
#La mayoria de números que se le ponen es en base a cordenadas del plano cartesiano.
t.speed(10) #Establece la velocidad en la que se irá mostrando los graficos.(va del 1 al 10)
t.circle(50)#Hará un circulo.
t.dot(10)#Establece el diametro (aplica en circulos)
t.showturtle()#Muestra la tortuga(puntero)
t.circle(100)
t.setx(100)#Moviliza la tortuga al eje x, pero su eje y no cambia. 
t.sety(100)#Moviliza la tortuga al eje y, pero su eje x no cambia.

turtle.done()