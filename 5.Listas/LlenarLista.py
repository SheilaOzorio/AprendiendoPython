lista = [1, 2, 3, 4]
lista2 = [ 5, 6, 7]

lista3 = lista + lista2
#Las listas no se pueden multiplicar pero sí sumar
print(lista3)
print('Esta es una lista de distintos datos: ', lista)

edad = int(input('Ingresa tu edad: '))
lista.append(edad)
# .append no sirve para ingresar datos a una lista (Esto para los datos imgresados por el usuario)

print(lista)

