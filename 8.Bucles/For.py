'''For cumple dos unicos objeticos, 1° Recorrer elementos iterables
2° Recorrer rangos, el elemento iterable es aquel al que se le permite
por medio de un iterador, tomar cada uno los valores que conforman a este
elemento , el más popular: la lista.  '''

lista = ['Uno', 'Dos', 'Tres', 'Cuatro']

for i in lista:
    print(i)
"""Aquí estamos diciendo: para in= lista,  que sería: recorre los valores de la lista entonces
 'i' primero va a tomar el valor del indice 0 que sería el uno, luego seguirá con el indicie 1
que es el 'Dos' y así hasta terminar, si imprimimos i  ya no se mostrará la lista a como era antes
pasa que el 'for' toma todos los datos que estan dentro de la lista, e 'i' que es nuestro
iterador va a tonar el valor de cada uno de los indices de la lista"""""

tupla= (1, 2, 3, 4, 5)
for j in tupla:
    print(j)

#Nuestra tupla aqui esta haciendo lo mismo que la lista
#En pocas palabras for nos ayuda a recorrer elementos iterables.

