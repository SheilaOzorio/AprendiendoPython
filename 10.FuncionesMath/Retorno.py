#La sintaxis que se usa es para devolver funciones debe ser así:
#Siempre debemos usar print para que ese dato se vea reflejado

'''def <nombre de la funcion> ():
    <sentencia>
     <return>'''

def entero():
    print('Este es un dato entero:')
    return 10
print(entero())
def decimal():
    print('Este es un dato decimal:')
    return 90.53
print(decimal())

#Seperando con coma también podemos crear variables
def asignacion():
    return 1, 2, 3, 4, 5, 6
#estamos igualando las variables a la funcion
a, b, c, d, e, f = asignacion()

print(b)
print(e)
#De esta forma 'a' le pertenece al valor 1, 'b' al 2, 'c' al 3 y así sucesivamente.
