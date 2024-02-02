#Crear una clase llamada Marino(), con un metodo que sea hablar, en donde muestre un mensaje que diga "Hola...", luego crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar por "soy un polpo". Por último, crear una clase llamada Focca(), heredado de Marino, pero que tenga un atributo nuevo llamado mensaje y que muestre ese mensaje como parametro.

class Marino():
    def hablar(self):
        print("Hola...")

class Pulpo(Marino):
    def hablar(self):
        print("Yo soy un pulpo")

class Foca(Marino):
    def hablar(self, mensaje):
        self.mensaje = mensaje
        print(self.mensaje)

marino = Marino()
marino.hablar()


pulpo =Pulpo()
pulpo.hablar()

foca = Foca()
foca.hablar("Hola, soy una foca")