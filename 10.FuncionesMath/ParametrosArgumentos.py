#La forma más común de usar variables es por medio de parametros y argumentos. Un parametro es una variable que se utiliza cuando se crea una función.  Un argumeto es el valor que se le asigna a un parametro cuando mandamos a llamar a la función. 
def suma():
    num1 = 20
    num2 = 30
    suma = num1 + num2
    return suma
print(suma())
#Esto es a como se hace usualmente
'''Siempre que mande a llamar a la función "suma" los valores serán los mismos, la suma siemre será 20 y 30, aquí es donde entran los parametros que son variables y los argumentos son los valores de la variable, estos nos sirven para la reutilización de código, es su primera utilidad '''

def suma1(num3 , num4):
    suma1 = num3 + num4
    return suma1
print(suma1(10, 35))
print(suma1(15, 80))

#Así se hace "reulilizando código", aquí nos ahorramos líneas de código y al agregar print y ponerle nuevos valores arroja los nuevos datos sin necesidad de agregar de nuevo otras variables.