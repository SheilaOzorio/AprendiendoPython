#Cuando querramos averiguar los valores de un atributo encapsulado, debemos de crear el método GEt o el método Getter por cada atributo. Primero creamos con el "edit" los atributos, es muy común que los métodos que vayamos a colocar lleven el mismo nombre de los atributos. NOTA importante: lo único que va a llevar por ser un método GET es un "return".


class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0
    @property

    def cuenta(self):
        return self._cuenta
    
a = A()
print(a.cuenta())  #Hacer el llamado de un atributo así como método es la la forma correcta.
#El metodo @property nos ayuda a ya no poner esos parentesis (a.cuenta >()< ), y de esa forma llamamos al método como si fuera atributo SIn coloacrle los parentesis
print(a.cuenta)
#Y esto es el método GET, es recomendable que cada atributo tenga su propio método   @PROPERTY.