#Errores que pueden salir de utilizar "herencia", que sería que algo  no se "herede" bien, para eso usaremos "super".
class Animales():
    def __init__(self, nombre):    #Aquí estamos pidiendo en un init que se ingrese el atributo de "nombre"
        self.nombre = nombre

class Perro(Animales):    #Al agregarle el primer class (animales),estamos haciendo que "Perro" herede sus atributos, en este caso heredaría el atributo "nombre"
    def __init__(self, nombre, sonido):
        super().__init__(nombre)   #Este super nos ayuda a evitar el posible error que podría pasar si no se"hereda " bien "nombre", que es nuestro atributo.
        self.sonido = sonido
perro = Perro("Firulais", "Guauuu!")  #Aquí estamos agregandole valores a los atributos, que sería "firulais" a "nombre" y "guauu" a "sonido"
print(perro.nombre)
print(perro.sonido)

#En ocasiones el método init  no se llega a heredar del todo, para eso nos sirve "super. " se agregaría así. "super." + el metodo que queremos agregar; ejemplo en la línea 8.