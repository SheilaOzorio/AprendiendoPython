'''Crear un programa que permita al usuario elegir un candidato por el cual votar.
Las posibilidades son: Candidato A por el partido Rojo, candidato B por el partido verde,
candidato C por el partido azul. Según el candidato elegido (A,B,C) se le debe imprimir
el mensaje "usted ha votado por el partido (color que corresponda  al candidato elegido)
si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles,
indicar "opción errónea"'''
#Pista
#Si la letra ingresada por el usuario es en minúscula, el programa debe convertirla en mayúscula.

opcion = input('Ingresa la opción de tu canditato (ABC): ')
if opcion.upper() == "A":
    print('Usted ha escogido al canditato Rojo')
elif opcion.upper () == 'B':
    print('Usted ha escogido al candidato Verde')
elif opcion.upper () == 'C':
    print('Usted ha escogido al candidato Azul')
else:
    print('Opción erronea')
