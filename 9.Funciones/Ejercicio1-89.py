'''Crea un programa que tenga una lista, luego crea una función con la cual
se van a pedir numeros al usuario para agregar a la lista. Debes crear una
segunda funcion en donde se ordenen los numeros pares e impares dentro de dos
listas nuevas'''
lista = []
num = 0
def pedir ():
    i = 0
    while i <= 5:
        num = float(input('Imgresa un numero: '))
        lista.append(num)
        i += 1
pedir()
print(lista)

def ordenar():
    lista.sort()
    pares = []
    inpares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            inpares.append(i)
    print(pares)
    print(inpares)
pedir()
ordenar()

# .sort no sirve para ordenar para ordenar datos
# .append nos sirve para agregar un elemento al final de la lista



    