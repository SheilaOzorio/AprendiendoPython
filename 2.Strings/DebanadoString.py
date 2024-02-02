#DEBANADO DE CADENA
cadena = "Este es un Ejemplo de Substring (Debanado de cadena)"
print((cadena[ 8 : 22]))
print(cadena[ : 53])  #En este caso aunque no le ponga un número incial, python lo tomartá como desde el 0
print(cadena[ -18]) #Aquí mostrará el caracter 18 empezando de derecha a izquierda
print(len(cadena))
'''En el ejemplo anterior la función de "len" nos sirve para hacer un conteo de los caracteres, en este caso de "cadena", si el agregamos [0 : 20],
estará haciendo el conteo del caracter 0 al 20, NOTA: el de la derecha nunca se mostrará, es decir que en realidad su conteo será del 0 al 19'''
#METODOS DE STRINGS

cadena1 = 'Estoy utilizaNdo los metodos de Python'
print(cadena1.lower())
print(cadena1.upper())
print(cadena1.capitalize())
print(cadena1.title())
print(cadena1.swapcase())

# .lower conVierte todo en misusculas 
# .upper convierte todo en mayusculas
# .capitalize cambia cada primera letra de cada palabra en mayusculas
# .swapcase convierte las munisculas en mayusculas y viceversa.
