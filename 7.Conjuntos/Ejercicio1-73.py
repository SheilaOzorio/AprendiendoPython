'''Escribir una tupla con los meses del año, luego pide al usuario un 
numero, el que haya ingresado es el mes que debo mostrar en la tupla'''

tupla = ('Enero', 'febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

mes = int(input('Ingresa el numero de tu mes: '))
mes -= 1
#Aquí estamos restandole uno ya que nuestro listado siempre comienza desde 0, es decir que si coloca 1 saldrá febrero y no enero
print('Tu mes es: ', tupla[mes])

#Otra forma de realizar la  misma operacion es:
'''print('Tu mes es: ', tupla[mes-1])'''



