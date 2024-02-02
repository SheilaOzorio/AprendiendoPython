#Un bucle consta de condicion, iterador/contador y sentencia. SIEMPRE debe contener un iterador, si un bucle no lleva un iterador este se rompe
'''Un iterador es una variable que va conforme a la condicion y cuenta las veces que
el bucle se debe de repetir'''
'''Como buena practica llamamos a nuestro iterador" con una i o con una j '''

i = 0
while i < 10: 
    i += 1     
    print('Estoy iterando, voy por el salto: {}'.format(i))

#Explicación del bucle: ¿Es i menor a 10?
'''Entonces aumenta esta i en 1, es decir que pasa de 0 a ser 1, y luego ejecuta este print, y el bucle sigue, después ese 1 pasa a ser 2 y así sucesivamente 
hasta llegar al ultimo que sea menor a 10, según nuestra formula'''

#Bucles: Estructuras repetitivas que a apartir de una condicion van generando un cambio.
#Aquí el orden de los factores sí altera el producto#