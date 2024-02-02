'''Hacer un programa que pida al usuario su nombre, su edad y su sexo
y que los muestre: '''
#Te llamas: 
#Tu edad es:
#Eres:

nombre = input('Ingresa tu nombre: ')
edad = int(input('Ingresa tu edad: '))
sexo = input('Ingresa tu sexo: ')

print('Te llamas: {}'.format(nombre))
print('Tu edad es: {}'.format(edad))
print('Eres: {}'.format(sexo))

#Otra forma de realizar lo mismo pero sin tantos "print" es:

print('Te llamas: {}\nTu edad es: {}\nEres: {}'.format(nombre,edad,sexo))
