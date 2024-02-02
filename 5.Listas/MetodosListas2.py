lista = ['Python', 12, 'Aprendiendo', 14, 'Disciplina']
#En caso de que querramos modificar un valor de la lista 
lista[2] = 'Aprendiending'
print(lista)
#Aqui ya se modifico el dato 2, paso d 'Aprendiendo' a 'Aprendiending'
lista.pop()
# .pop elimina el ultimo valor de la lista
print(lista)
lista.remove('12')
print(lista)
# .remove se encarga de eliminar el valor que yo
