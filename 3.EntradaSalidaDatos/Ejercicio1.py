'''Realizar un programa que haga el proceso de formula general
para la resolucion de ecuaciones, sabiendo que la formula 
general es la que está en la imagen, el usuario debe ingresarlos
valores de "a",  "b", "c" y el programa debe hacer el proceso
 para que al final muestre el mensaje,
 #3x^2 - 5x+2=0     x=1 x=2/3'''

from math import sqrt
print(sqrt)
A = int(input('Ingresa el valor de A: '))
B = int(input('Ingresa el valor de B: '))
C = int(input('Ingresa el valor de C: '))

x1 = 0
x2 = 0

if ((B**2)-(4*A*C)) < 0:
    print ('No se puede ejecutar porque no se puede sacar raiz a un número negativo')
else:
  x1 = (-B + sqrt((B**2)-(4*A*C)))/(2*A)
  x2 = (-B - sqrt((B**2)-(4*A*C)))/(2*A)
print("La solucion es : \nx1=" ,x1,"\nx2 ", x2)

