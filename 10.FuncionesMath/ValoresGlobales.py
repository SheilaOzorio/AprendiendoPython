#Para tener una función que se quede estática (que no cambie), es decir que querramos tener una funcion que tenga los mismos valores siempre. Podemos hacer:

def valores():
    global valores
    num1 = 110
    num2 = 40
    resultado = num1 + num2
    return resultado 
print (valores())
#En el ejemplo anterior las variables num1 y num2 que están dentro del argumento "valores", no hay forma de acceder a ellas desde afuera, es decir que sólo están definidas en "valores" y en el print que está "afuera", me va a marcar error. Para evitar esos errores y poder acceder a un parametro dentro de un argumento usaremos "Global" seguido del nombre de la variable. Ejemplo : global num1, y ahora ya mostrará el valor de num1 que es 110.
#No podemos crear la varianle y asignarle el valor cuando usmos global, primero hay que englobarlo y después asignarle el valor, si no devolverá la sintaxis de error.



