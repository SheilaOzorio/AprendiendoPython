#El método "herencia" es dos o más clases y que unas hereden a otras, métodos que pasen de la clase padre a la clase hija, es decir métodos que se hereden sin necesidad de que sean colocados de nuevo o bien sin que sean mandados a llamar una vez más.
# "pass" es una forma de decirle a python que no vamos a colocar nada y que le dejemos en paz por el momento :x

class Animales():
    def habla(self):
        print('Yo soy un animal')

    def descripcion(self):
        print("Yo soy una {}".format(self.animal))
class Perro(Animales):
    pass

class Abeja(Animales):
    def __init__(self, animal):
        self.animal = animal

Animal = Animales()
Animal.habla

perro = Perro()
perro.habla

abeja = Abeja("Abeja")
abeja.descripcion()
