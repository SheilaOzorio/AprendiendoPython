#Crear un programa con tres clases Universidad, con atributos de nombre(donde se almancena el nombre de Universidad). otra llamada Carrera con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima llamada Estudiante, que tenga como atributos su nombre yu edad. El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto como persona.

class Universidad():
    def __init__(self, name):
        self.name = name

class Carrera():
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Student(Universidad, Carrera):
    def datos(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print("Mi nombre es {}, tengo {}, mi especialidad es: {} Estudie en: {}".format(self.nombre, self.edad, self.especialidad, self.name))

persona = Student("UNAM")
persona.carrera("Sistemas")
persona.datos("Lolita", 23)


        
