'''El rango nos va a marcar o delimitar un punto en especifico en el que un bucle
va a recorrerse, amerita DOS argumentos, su función es tipo: " inicio, recorrido y
final" '''
"""Con las listas, tuplas diccionarios el bucle FOR va a llevar tanto como el bucle 
contenga objetos, quiere decir que si una lista tiene 10 elementos el bucle for va a
llegar entonces hasta esos 10 elemetos. PERO 'range' toma un punto de inicio y
un punto final."""
#Ejemplo: en este caso aunque no estén los demás numeros sabrá que debe terminar en 10 
#No hay que olvidar que el elemento de la derecha será ignorado, si quermos que
#aparezca el 10 entonces debemos poner 11
#si agregamos en tercer argumento, este va a determinar la cuenta en la que proseguira
#Si agregamos el 2, entonces irá de 2 en 2.
#Si colocamos numeros negativos, el numero más grande debe ir primero, justo por ser negativos

for i in range(1, 10, 2):
    print(i) 