'''Escribe un programa que pida dos palabras y diga si riman o no.
Si coinciden las tres ultimas letrass tiene que decir aue riman. Si cóinciden 
sólo las últimas tiene que decir que riman un poco y si no, que no riman'''

#Serán 4 condiconales

palabra1 = input('Ingresa la primer palabra: ')
palabra2 = input('Ingresa la segunda palabra: ')
'''Lo primero que debemos saber para que la condición se cumpla es la cantidad
de carácteres de la palabra, esto debido a que las palabras con menos de tres caracteres
no riman nunca, por lo tanto usaremos 'len' que nos sirve para contar'''

if len(palabra1) < 3 or len(palabra2) < 3:
    print('No rima porque tiene menos de 3 caracteres')
elif palabra1[-3 : ] == palabra2[-3 : ]:
    print('Las palabras riman!!')
elif palabra1 [-2 : 0] == palabra2[-2 : ]:
    print('Las palabras riman poco')
else:
    print('Las palabras no riman :c ')
#Recordando que si ponemos un número negativo Ejem: [-3], se estará contando hacia atrás.
#De esta froma logramos nuestro cometido, ya que lo que queremos buscar en la palabra agregada por el usuario son las últimas letras.