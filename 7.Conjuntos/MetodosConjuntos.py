#Se recomienda abrir un conjunto con llaves {}
#Los conjuntos no muestra los datos repetidos
conjunto = {1, 2, 3, 4, 5}

conjunto.add(20)
# .add nos permite agregar un elemento más al nuestro conjunto
print(conjunto)

conjunto.remove(1)
print(conjunto)
# .remove elimina un elemento del conjunto que le asignemos

conjunto.pop ()
print(conjunto)
# .pop elimina cualquier elemento de nuestro conjunto al azar

conjunto.update([12, 13, 14, 15])
print(conjunto)
# .upate añade elemtn iterables, 'Iterable' es aquel elemento que se puede recorer con un ford/bucle

conjunto.clear()
print(conjunto)
# .clear limpia nuestro conjunto, es decir que elimina todos los elementos que contiene
