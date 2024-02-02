#El hecho de que tengamos nuestros valores ya con el método GET, no significa que podemos modificar los valores, para eso nos sirve el método SET para cada atributo que se le quiera cambiar  colocar o modificar el método, debemos colocar SET que sería: -@-  -el nombre del atributo a cambiar- y -.setter- Ejemplo: @cuenta.setter
#Es recomendable que el nombre del método sea el mismo que del atributo.
class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0
    @property
    def cuenta(self):
        return self._cuenta
    
    @cuenta.setter
    def cuenta(self, cuenta):
        self._cuenta = cuenta

    @property
    def contador(self):
        return self._contador
    
    @contador.setter
    def contador (self, contador):
        self._contador = contador

a = A()
print(a.cuenta)
a.cuenta = 20
print(a.cuenta)
a.contador = 23
print(a.contador)
#En el ejemplo de la línea 11 estamos colocando "def" seguido del atributo a cambiar y el metodo SETTER, pese a que tenga el mismo nombre la diferencia va a ser los parametros que este va a recibir, que es el self, el atributo a cambiar, esto entre parentesis y los dos puntos, en la siguiente líena el self._ seguido del atributo a cambiar e igualado al nuevo valor que va a recibir. Ejemplo en las líneas  19 a la 21. Luego por fuera de la clase le damos el valor que queremos que tenga e imprimimos. Ejemplo de cómo debería de ser en la línea 25 y 26.
#Cuando un atributo tiene sólo el método GET y no el método SET, se le llama a ese un atributo "redondee", es decir sólo lectura no modificación. 
#Usualmente no debe falta el método GET ya que casi siempre se utiliza.