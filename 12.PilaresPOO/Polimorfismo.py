#polomorfismo es la modificación de métodos cuando se herendan de otras clases,también se le puede llamar polimorfismo a crear objetos que apunten o que usen el mismo método pero que el objeto sea diferente; digamos que tengo un objeto 1 y un objeto 2, y ambos están herdando una clase padre, ambos objetos oueden ejecutar un método por ejemplo "habla" pues en ese caso ambos estarían ejecutando ese método, estarían entonces técnicamente ejecutando el mismo método dos objetos diferentes.

class Animales():
    def __init__(self , mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Yo no hablo")
#Este es un ejemplo del polimorfismo, ya que estamos cambiando un valor; de "mensaje" pasa a ser "Yo no hablo"
class Pez(Animales):
    def hablar(self):
        print("Yo tampoco hablo")
#Este es otro ejemplo de polimorfismo, ya que estamos modifiacando su valor.
perro = Perro("Guauu!") #Aquí se ejecuta el método modificado y no el heredado
perro.hablar()

animal = Animales("Miauu")
animal.hablar()

pez = Pez("Nadaremos , nadaremos, en el mar el mar el maaarrr")
pez.hablar()
