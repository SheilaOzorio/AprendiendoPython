'''Realizar un programa que conste de una clase llamada "Estudiante", que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar los atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no. '''

class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print("Nombre: {} \nNota: {} ".format(self.nombre , self.nota))
    def resultado(self):
        if self.nota < 6:
            print("Lo siento, estás REPROBAD0")
        else:
            print("Felicidades, estás APROBADO")

estudiante1 = Estudiante ("Alejandro" , 9.8)
estudiante1.imprimir()
estudiante1.resultado()
estudiante2 = Estudiante("Pedrito" , 5)
estudiante2.imprimir()
estudiante2.resultado()
