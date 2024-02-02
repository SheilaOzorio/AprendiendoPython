lista = [1, 2, 2, 2, 2, 3, 4, 5]
print(lista)
#Para agregar más datos a mi lista debe usar el método 'append' y entre parentesis ponemos los datos a agregar
lista.append(6)
#Primero mandamos a llamar a la lista seguido de .append y los datos a agregar
print(lista) 
#Para agregar un dato que queremos en un lugar en especifico de la lista agregar .insert seguido del lugar en que queremos el dato, y el dato

lista.insert(2, 2.5)
print(lista)
# .count nos sirve para contar algún elemento de la lista
lista.count(2)
#Aquí nos muestra cuantos 2 hay en la lista
print(lista.index(4))
# .index nos ayuda a buscar el primer 4 de la lista
lista.sort()
# .sort nos sirve a ordenar nuestra lista
lista.reverse()
# .reserve nos sirve para imprimir la lista de forma contraria a sus orden inicial.


