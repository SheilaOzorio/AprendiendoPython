'''Crear una función que pida dos números. Si el primero es mayor que el segundo
el programa debe retornar el valor 1; si el segundo es mayor que el primero, debe 
retornar -1; si ambos son iguales, debe retornar 0.'''

def numero():
    num1 = float(input('Ingresa el 1er número:'))
    num2 = float(input('Ingresa el 2do número:'))

    if num1 > num2:
        return 1
    elif num2 > num1:
        return -1
    else:
        num1 == num2
        return 0
print(numero())

    
