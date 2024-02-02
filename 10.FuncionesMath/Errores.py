#En este ejemplo se muestra esa pregunta esperando que le usuario tal vez se equivoque al poner el valor solicitado, 'int', no indica que debe recibir el valor en número, en dado caso que ingrese un strimg, el comando 'try' que es 'intentar', nos ayuda a que si en caso de que el usuario cometa algún error, puede volverlo a intentar hasta que sea lo correcto, usaremos 'except' seguido de un print, para que cuando cometa ese posible error imnprima algo que tu le coloques para hacerle saber al usuario que está comentiendo un error, seguido de eso imprimirá de nuevo la solicitud inicial para que empiece otra vez; lo malo de eso es que si el usuario se vuelve a equivocar ya no volverá a salir la leyenda que pusiste en 'except', es decir que sólo paracerá una única vez, para solucionar eso usaremos un bucle 'while true', mientras sea verdadero se ejecutará todo el resto del código, tenemos que colocar también 'break' para evitar que nos siga preguntando incluso si ya pusiste lo que se espera. De esta forma evitaremos que nuestro bucle sea eterno.
#El comando finally, nos sirve para poner alguna leyenda que indique que la función ha terminado, posiblemente no sea tan útil ya que haya o no error, seguirá apareciendo la función 'finally' junto con los que contiene.

while True:
    try:
        edad= int(input('Ingresa tu edad: '))
        print('Tu edad es: ', edad)
        break
    except:
        print('Ingresaste un valor erroneo')
    finally:
        print('Las preguntas terminaron')

