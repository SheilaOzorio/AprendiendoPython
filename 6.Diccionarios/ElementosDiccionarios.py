diccionario = {'nombre' : 'Sheila', 'Apellido' : 'Ozorio', 'Estatura' :  1.60, }
print(diccionario)
print(diccionario.keys())
# .keys nos devuelve las claves/llaves que en este ejemplo será 'nombre', 'apellido' y 'estatura'
print(diccionario.values())
# .values nos devuelve nada mas los valores, en el ejemplo sería 'Sheila', 'ozorio' y 1.60
print(diccionario['Estatura'])
#En este ejemplo estamos piediendo que nos devuelva el valor de una sóla llave de nuestro diccionario.

diccionario['Peso'] = '57 kg'
#De esta forma se agrega un nuevo valor a nuetsro diccionario
print(diccionario)
diccionario['nombre'] = 'Cordelia'
#De esta forma se modifica un valor ya existente en nuestro diccionario
print(diccionario)

