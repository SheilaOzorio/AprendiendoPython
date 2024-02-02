'''Pedir al usuario que ingrese dos numeros, después, se debe mostrar el
rango de esos dos numeros, pero, solo imprimiendo las numeros que sean 
impares'''

num1 = int(input('Agrega el 1er numero: '))
num2 = int(input('Agrega el 2do numero: '))

for i in range( num1, num2 +  1):
 
  if i % 2 == 0:
     continue
  print(i)

'''Si i es modulo de la división entre 2 es igual a 0 (if i % 2 == 0:), va a hacer
la division entre 2 y va a evaluar si el residuo es cero, si esto 
ocurre es par, caso contrario es inpar, por ende colocamos 'continue' para que 
se salte cada vez los numeros que sean pares  y que no nos sirven.
'''