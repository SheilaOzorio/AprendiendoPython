diccionario = {1 : 2 , 2 : 3 , 3 : 4}
diccionario2 = {4 : 5, 5 : 6 , 6 : 7}

print(diccionario)
diccionario.pop(3)
# .pop eliminará la clave que le dimos junto con su valor. En este caso eliminará 3 : 4
print(diccionario)
diccionario.clear()
# .clear nos permite borrar todos los datos del diccionario
print(diccionario.get(2))
# .get no sirve para traer un valor en especifico en este caso nos traerá el valor de la llave 2 que sería 3, según nuestro diccionario

diccionario.setdefault(11 , 51)
# .setdefault no sirve para agregar una nueva llave con au respectivo valor a nuetsro diccionario
print(diccionario)

diccionario.update(diccionario2)
# .update nos sirve para unificar en caso de tener má de un diccionario
#En caso de que haya algúna llave repetida sólo se mantendrá una.
print(diccionario)

diccionario.copy()
print(diccionario)
# .copy nos genera una copia del diccionario


