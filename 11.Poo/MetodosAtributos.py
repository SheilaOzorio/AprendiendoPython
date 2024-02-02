#Un metodo es una función dentro de una clase, es como una acción que puede tener un objeto o que puede realizar

class FabricaTelefonos():
    marca = 'Huawei'
    color = 'Azul'
    mermoraRam = 32
    almacenamiento = 128


    def llamar(self , mensaje):
        return mensaje
    
    def escucharMusica(self):
        print('Estas escuchando musica')
    
telefono = FabricaTelefonos()
telefono.color
print(telefono.marca)
telefono.mermoraRam
telefono.almacenamiento
print(telefono.llamar('Hola qué tal?'))
telefono.escucharMusica()
#Aquí dentro de la clase, yo poseo el metodo y por fuera ahora yo mando a llamar a ese metodo como el telefono.llamar con su respectivo mensaje

#Así es como podemos agregarle atributos a mi class
#Los metodos son funciones que pueden realizar un obje


 
 