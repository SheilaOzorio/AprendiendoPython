#Ahora la forma correcta del encapuslamiento es por medio sólo un guión bajo.
class A():
    def __init__(self):
        self._contador = 0
        self._cuenta = 0

    def incrementar(self):
        self._contador += 1
    
    def cuenta(self):
        return self._contador
    
a = A()
print(a.cuenta)

