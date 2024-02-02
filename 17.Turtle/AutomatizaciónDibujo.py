import turtle

s = turtle.Screen()
t = turtle.Turtle()
i = 0

'''t.forward(90)
t.right(90)
t.forward(90)
t.right(90)
t.forward(90)
t.right(90)
t.forward(90)'''

"""Este es un cuadrado que de igual forma se puede hacer con .forward, .right, .left, pero
estamos automatizando este proceso por medio de un bucle for"""

'''for i in range(4):
    t.forward(100)
    t.right(90)'''
t.forward(50)

while i <= 100:
    t.circle(i)
    i += 10


turtle.done()