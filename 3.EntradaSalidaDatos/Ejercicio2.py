'''Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha tenido
un alumno en un determinado curso, conociendo las notas de: 
tres practicas, el examen parcial y el examen final'''
 #Considere
 #PP = (P1+P2+P3)/ 3 PROM = (PP + 2EP + 3*EF)/6
 #Donde: P1, P2, P3 : Practicas
 #PP : Promedio practica
 #Prom: Promedio
 #EP: Examen parcial
 #EF: Examen final

practica1 = float(input('Ingrese el valor de la practica 1: '))
practica2 = float(input('Ingresa el valor de la practica 2: '))
practica3 = float(input('Ingresa el valor de la practica 3: '))
Examenparcial = float(input('Ingresa el valor del examen parcial: '))
ExamenFinal = float(input('Ingresar valor de examen parcial: '))

promedioPractica = (practica1 + practica2 + practica3) /3
PromedioFinal = (promedioPractica +2* Examenparcial + 3*ExamenFinal)/6
print('El promedio de prcatica del estudiante es de:\n ' , promedioPractica, '\n Y el promedio fional es de :\n ', PromedioFinal )