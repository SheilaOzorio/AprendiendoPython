nombre = input('Ingresa tu nombre: ')
edad = int(input('Ingresa tu edad: '))

print(nombre)
print(edad)

#Esto es una concatenacion
print(nombre, edad)
print('Hola', nombre, 'tienes', edad )

#Otra forma de unir datos
print('Hola {} tienes {}'.format(nombre,edad))