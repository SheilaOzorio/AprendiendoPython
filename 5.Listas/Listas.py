#La sintaxis para una lista son estas llaves []
#A las listas le podemos agregar cualquier dato (letras, numeros enteros y con decimal)
lista = ['Python', 120, 'Nombre', 3.1416, 2031, 'Soy estudiante', 'Hola mundo']
print(type(lista))

#El primer dato de las listas siempre empieza con 0, en el ejmplo anterior 'Python' sería el 0 y no el 1ero.
#A las listas sí le podemos cambiar los datos

print(lista[5])
print(lista[0 : 5])
print(lista[ : 2])
#Al dejar un espacio vacío, el prograna unterpretará que noostros queremos empezar desde el primero, el dato 0b que es 'Python'
print(lista[-1])
#Si usamos un números negativo me mostrará  desde el ultimo dato hacia atrás.
print(lista[-2 : -5])

