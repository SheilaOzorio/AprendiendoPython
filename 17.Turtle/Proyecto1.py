import turtle
import random

s= turtle.Screen()
s.title('Proyecto 1')
s.bgcolor('grey')


jugador1= turtle.Turtle()
jugador1.hideturtle()
jugador2 = turtle.Turtle()
jugador2.hideturtle()

jugador1.speed(3)
jugador2.speed(3)

jugador1.pensize(3)
jugador2.pensize(3)


jugador1.shape('turtle')
jugador1.color('purple')

jugador2.shape('turtle')
jugador2.color('red')


jugador1.penup()
jugador1.goto(200, 200)
jugador1.pendown()
jugador1.circle(30)
jugador1.penup()
jugador1.goto(-300, 225)
jugador1.showturtle()


jugador2.penup()
jugador2.goto(200, -200)
jugador2.pendown()
jugador2.circle(30)
jugador2.penup()
jugador2.goto(-300, -180)
jugador2.showturtle()

dado = [1,2,3,4,5,6]

for i in range(20):
    if jugador1.pos() >=(165, 180):
        print('La tortuga morada es la ganadora')
        break
    elif jugador2.pos() >=(165, -180):
        print('La tortuga roja es la ganadora')
        break
    else:
        turno1 = input('Presiona la tecla enter para que avance la tortuga morada')
        turno1 = random.choice(dado)
        print ('Tu número es ', turno1, '\nAvanzas: ',turno1*20)
        jugador1.pendown()
        jugador1.forward(20*turno1)
        
        
        turno2= input('Presiona la tecla enter para que avance la tortuga roja')
        turno2 = random.choice(dado)
        print('Tu número es: ', turno2, '\nAvanzas: ', turno2*20)
        jugador2.pendown()
        jugador2.forward(20*turno2)
        
turtle.done()