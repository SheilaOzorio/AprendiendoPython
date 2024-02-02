'''Escribir un programa que, dado un numero entero, muestre su valor absoluto.
Nota: para los numero positivos su valor absoluto es igual al numero
(el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número
multiplicado por -1(el valor absoluto ede -52 es 52)'''
#El valor absoluto de un numero es el valor positivo de un numero. 78 = 78
# >abs< es un metodo python que se encarga de sacar el valor absoluto de un numero.
#Es decir que hara la funcion que necsitamos, resumiendo el codigo de abajo.
print(abs(-5))


numero = int(input('Ingresa un  numero ENTERO: '))
if numero > 0:
#En esta funcion decimos: si numero(que es el numero que ingresa el ususario) es mayor'>' a 0, que imprima lo demas. 
    print('El valor absoluto de {} es: {}'.format(numero, numero))
#Se agrega '{}' en este caso, para tomar en cuenta lo que ingresa el usuario.
else:
    print('El valor absoluto de {} es: '.format(numero), numero * -1)
# otra forma se usar >abs<
    print('El valor absoluto de {} es: {}'.format(numero,abs(numero)))
    

