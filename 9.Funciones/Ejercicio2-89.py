'''Escribe una función que reciba un numero entero positivo y devuelva
su factorial.'''
from math import factorial

def factorial():
    num = int(input('Ingresa un numero entero y positivo:  '))
    if num > 0:
        factorial = 1
        for i in range(1 , num + 1):
            factorial = factorial* i
        print(factorial)
    else:
     print('El número es negativo y no podemos proceder')
