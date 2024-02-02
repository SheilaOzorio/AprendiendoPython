#Escribir una función que reciba una muestra de números en una lista y devuelva su medida.


def medida(*tupla):
    print(len(tupla))
medida(10, 20, 30, 40, 50)

def size(*tupla2):
    return len (tupla2)
print(size(15, 30, 70, 50, 10, 15))