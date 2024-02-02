'''Escribir un programa que pida un numero al usuario y muestre
las tablas de multiplicar '''

tabla = int(input('Ingresa un numero para saber su tabla de multiplicar: '))
i = 1
multi = 0

while i <= 10:
    multi = tabla * i

    print('{} x {} = {}'.format(tabla, i, multi))
    i += 1
    
#Explicación
''' i empieza en 0, entonces pregunta... ¿es i menor o igual a 10? (while i <= 10:) sí, porque i vale 0
Entonces realiza esta multiplicacion, tabla (que es igual al numero que el usuario dijito) dijitamos 8,
entonces 8 por i ( multi = tabla * i) como el valor de i es 0, entonces 8 x 0, y eso da como resultado 0
ahora imprime primero el numero que el usuario dijitó, multiplicalo por i
 y que el resultado sea la multipicación de ambos numeros ( print('{} x {} = {}'.format(tabla, i, multi)), 
 ahora a esa i del principio sumale un 1 (i += 1), entonces vuelve a preguntar y el bucle empieza de nuevo , 
 ¿es i menor o igual a 10?, ahora i ya vale 1 y se vuelve a multiplicar el 8 por el 1, y cuando la i sea ya no menor ni igual a 10,
 es decir que sea mas, ahora el bucle podrá terminar, y tendremos al fin el resultado esperado que es la tabla del 8 '''
