'''Las tupla es una lista que no se puede modificar, es su primera diferencia de las listas '''
#Las tuplas no tiene metodos tan utilizados ya que lo que contiene no se pueden cambiar
# podemos escribir una tupla con parentesis y si parentesis(), en ambos casos python la reconoceras como una tupla

tupla = (1,2, 3, 4, 5)
tupla2 = (6, 7, 8, 9, 10)
print(tupla)
print(type(tupla))
print(tupla[2]) 
# De esta forma estamo accediendo al dato 2, que según los datos de la tupla sería el 3
print(tupla[ 0 : 4])
print(tupla + tupla2)
# Aquí estamos concatenando/sumando nuestras tuplas
