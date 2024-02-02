#Videojuego de la serpiente.

import turtle
import time
import random

retraso = 0.1
marcador = 0
marcador_alto = 0

#Preparando pantalla.
s = turtle.Screen()
s.setup(650, 650)
s.bgcolor('black')
s.title('Snake')

#Definiendo serpiente
serpiente = turtle.Turtle()
serpiente.speed(1)
serpiente.shape('square')
serpiente.penup()
serpiente.goto(0, 0)
serpiente.direction = 'left'
serpiente.color('green')

#Comida
food = turtle.Turtle()
food.shape('circle')
food.penup()
food.color('red')
food.goto(0, 50)
food.speed(0)

#Lista vacía que almacenará los movimietnos de la la serpiente
body = []

texto = turtle.Turtle()
texto.speed(0)
texto.color('white')
texto.penup()
texto.hideturtle()
texto.goto(-200, 300)
texto.write('Marcador: 0 \tMarcador más alto: 0', align='left', font=('calibri', 24, 'normal'))

#Definiendo cada movimiento.
def up():
    serpiente.direction = 'up'
def down():
    serpiente.direction = 'down'
def right():
    serpiente.direction = 'right'
def left():
    serpiente.direction = 'left'
    
#Obteniendo las coordenadas respectivas de cada 
def movimiento():
    if serpiente.direction =='up':                  
        y = serpiente.ycor()
        serpiente.sety(y + 20)
    elif serpiente.direction =='down':
        y = serpiente.ycor()
        serpiente.sety(y - 20)
    elif serpiente.direction =='right':
        x = serpiente.xcor()
        serpiente.setx(x + 20)
    elif serpiente.direction =='left':
        x = serpiente.xcor()
        serpiente.setx(x - 20)
        
#Haciendo que el teclado responda a los movientos del usuario.
 
s.listen() #Está pendiente si se oprime una tecla
s.onkeypress(up, 'Up')                              #Se debe colocar en mayúsculas la primera letra para indicar que se refieren a las TECLAS de arriba, abajo etc.
s.onkeypress(down, 'Down')
s.onkeypress(right, 'Right')
s.onkeypress(left, 'Left')
 


while True:
    s.update()
    
    #Haciendo que la serpiente se reinicie si choca con los bordes.
    if serpiente.xcor() >300 or serpiente.xcor() <-300 or serpiente.ycor() > 300 or serpiente.ycor() < -300:
        time.sleep(2)
        for i in body:
            i.clear()
            i.hideturtle()
        serpiente.home()
        serpiente.direction = 'stop'
        body.clear() 
        
        marcador = 0
        texto.clear()
        texto.write('Marcador: 0 \tMarcador más alto: 0', align='left', font=('calibri', 20, 'normal'))
    
   #Determinando en qué parte de la pantalla podrá aparecer la comida por medio de las coordenadas de 'X' y 'Y' 
    if serpiente.distance(food) < 20:
        x =random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)
    
    #Haciendo que el cuerpo de la serpiente crezca por medio de append. (Debemos recordar que 'body' es una lista)   
        new_body = turtle.Turtle()
        new_body.shape('square')
        new_body.color('green')
        new_body.penup()
        new_body.goto(0,0)
        new_body.speed(0)
        body.append(new_body)
        
        marcador += 10
        if marcador + marcador_alto:
            marcador_alto = marcador
            texto.clear()
            texto.write('Marcador:{}\tMarcador más alto:{}'.format(marcador, marcador_alto), align='left', font=('calibri', 24, 'normal'))

#Seguiendo el cuerpo de la serpiente.       
    total = len(body)
    for i in range(total -1, 0, -1):                #Con este "-1" estamos diciendole a la lista que recorra los nuevos elementos a la inversa, es decir hacia atrás.
        x = body[i-1].xcor()                        #Lo mismo sucede con este "i -1" manda los nuevos elementos hacia atrás. El .xcor y el ycor nos devolverá sus respextivas corrdenadas.
        y = body[i-1].ycor()
        body[i].goto(x, y)                          #Aquí mandamos las coordenadas recibidas de 'x' y 'y' a nuestro 'body'
            
    if total > 0:                                           
        x = serpiente.xcor()
        y = serpiente.ycor()
        body[0].goto(x, y)

        
    movimiento()
   #Determinado que la serpiente se reinicie si choca con ella misma 
  
    for i in body:
        if i.distance(serpiente) < 20:              #Si la distancia en la 'serpiente' es menos de 20, borra todo, oculta la serpiente y regresa a la serpiente al home (0,0)
            for i in body:
                i.clear()
                i.hideturtle()
            serpiente.home()
            body.clear()
    
    time.sleep(retraso)                             #Con esto nos aseguramos de que cuando la "serpiente" se mueva, haga un pequeño delate


turtle.done()