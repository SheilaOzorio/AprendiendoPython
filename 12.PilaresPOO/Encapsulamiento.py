#El encapsulamiento es aplicar a sobre los atributos cierto alcance para que ese atributo sea utilizado dentro de la clase, NO por fuera, NO en otra clase, sino SOLO dentro de la clase. Nos sirve para evitar el desvordamiento de memoria y para evitar ejecuciones innecesarias.

class A():
    def __init__(self):
        self.contador = 0


    def incrementar(self):
        self.contador += 1
        
    def cuenta(self):
        return self.contador
print('Objeto 1')   
a = A()
a.incrementar()
print(a.cuenta())


class B():
    def __init__(self):
        self.__contador = 0


    def incrementar(self):
        self.__contador += 1
        
    def cuenta(self):
        return self.__contador
    
print('Objeto 2')
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())
print(b.__contador())
#Es importante poder diferenciar al método del atributo
#El encapsulamiento es un atributo que no puede ser accedido por fuera de la clase.
#La forma de decirle a Python que "No permitas que se acceda desde afuera" es ponerle doble guión. Ejemplo en la clase B
# Cuando nosotros agregamos doble guión bajo a un atributo al inicio lo estamos encapsulando, es decir que es como ponerlo "privado" y que este sólo pueda ser accedido desde la misma clase.
#La forma de estrictamente decirle a Python "no permitas que se accede desde afuera", es ponerle doble guión bajo. Es decir quie hacerlo como en la línea 35 está mal, ya que estamos accediendo al atributo desde afuera, es por eso que nos arroja un error.