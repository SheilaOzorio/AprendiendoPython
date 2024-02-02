'''Def es una funcion propia de python, que muestra su resultado incluso sin haber 
usado print, todas las sentencias que tengamos dentro de la funcion se van 
a ejecutar cada vez que mandemos a llamar a la funcion, esto significa que podemos
ahorrarnos muchas líneas de codigo, una vez tengamos la funcion nos podemos ahorrar ese codigo, trabajo y memeria :) '''

def saludo():
    print('Hola Sheila')

saludo()
saludo()
saludo()
#Los parentesis son para que se distinga de una variable 
def tabla7 ():
    for i in range(1, 11):
        print("7 x {} = {}".format(i, i*7))
tabla7()