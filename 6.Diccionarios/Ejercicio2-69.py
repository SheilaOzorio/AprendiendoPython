'''Con el siguiente diccionario, debes crear un programa que pregunte al
usuario por un numero; el programa debe imprimir el jugador al que hace
referencia ese numero'''

diccionario = { 1 : 'Casillas' , 3 : 'Pique' , 5 : 'Puyol' , 11 : 'Capdevilla' , 14 : 'Xavi Alonso' , 16 : 'Busquets' , 8 : 'Xavi Hernandez' , 18 : 'Pedrito'}
jugador = int(input('Ingresa un número y te mostraré a qué jugador pertenece: '))


if jugador in diccionario:
    print(diccionario[jugador])
else:
    print('No se encuentra en el diccionario')
