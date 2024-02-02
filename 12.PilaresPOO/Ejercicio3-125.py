#Crear una clase Fabrica que tenga los atributos de Llantas, color y precio; Luego crear dos clases más que hereden a Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por último, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno.

class Fabrica():
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio
    

class Moto(Fabrica):
    def datos (self):
        print("La cantidad de llanta es de la moto: ", self.llantas)
        print("El color de la moto es: ", self.color)
        print("El precio de la moto es de:$", self.precio)

class Carro(Fabrica):
    def cifra(self):
        print("La cantidad de llantas del carroes de: ", self.llantas)
        print("El color del carro es: ",self.color)
        print("El precio del carro es de:$", self.precio)

moto = Moto(2, "rojo", 25000)
moto.datos()

carro = Carro(4, "gris", 50000)
carro.cifra()



