'''Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario
dos numeros y mostrar el rango de numeros entre ambas cifras'''

for i in range(1, 11):
    print(i)
num1 = int(input('Ingresa el 1er numero: '))
num2 = int(input('Ingresa el 2do numero: '))

for i in range(num1, num2 + 1):
    print(i)

'''Como queremos un rango, usamos entonces 'range'. Agregamos el + 1 al final ya que
el valor de la derecha nunca es contado, ahora el valor de la derecha sera el uno
por lo tanto el no contado sera ese 1'''