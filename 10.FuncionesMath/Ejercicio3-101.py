#Crea un programa que tenga dos funciones, una que contenga el área de un cuadrado con argumentos de base y altura; y otra el área de un circulo con argumento de radio.

def areac(altura, base):
    resultado = altura * base
    return(resultado)
print(areac(20, 20))

def radioCirculo ( 3.14 , radio):
    return( radio **2)
print(radioCirculo(3.1416, 10))