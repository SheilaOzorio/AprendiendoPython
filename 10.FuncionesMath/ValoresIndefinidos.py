#Hay parametros que van a ser un díjito, un número, una cedena de texto y sólo eso, en cambio hay otros que pueden llegar a ser más largos como tuplas y listas. Para eso tenemos que tener cuidado en su declaración.

def argumento(num):
    return(type(num))
print(argumento(10))

#De esta forma se le asigna un valor y luego se ve qué tipo de dato es (type), PERO si le agregamos un * ( def argumento(*num)) y automaticamente cualquier tipo de dato que le pases se convertirá en una tupla, aunque sea sólo un valor. 

