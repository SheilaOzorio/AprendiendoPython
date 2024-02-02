'''Escribe una lista que tenga los números de 1 al 10. Luego, debes hacer
que los datos que están en las posiciones 4,7 y 9 sean multiplicados 
por 2; por último, mostrar la lista con los datos nuevos '''

#Tomando en cuanta que la lista siempre empieza desde el 0, usaremos entonces el 3,6 y 8 para cambiar los numeros 4,7 y 9

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Esta es una forma de hacer la multiplicacion
lista[3] = lista[3]*2
#Esta es otra forma de multiplicar
lista[6]*= 2
lista[8]*= 2

print(lista)
