'''Escribir un programa que pregunte al usuario su edad y  el 
año en qué nació y muestre un listado de su edad con el año
en que cumplió esa edad (desde el 1 hasta su edad)'''

edad = int(input('Agrega tu edad: '))
year = int(input('Agrega el año en que naciste: '))
i = 1
while i <= edad:
    year2 = year + i
    print('Has cumplido: {} en: {}'.format(i, year2))
    i += 1 