#Realizar un programa en el cual se declaren valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un metodo para cada una e imprimir los resultados obtenidos. Llamar a la clase calculadora.

class Calculadora():
    def __init__(self):
        self.num1 = int(input("Ingresa un numero entero: "))
        self.num2 = int(input("Ingresa otro numero: "))

    def suma(self):
        self.suma = self.num1 + self.num2
        return "La suma da como resultado: ", self.suma

    def resta(self):
        self.resta = self.num1 - self.num2
        return"La resta da como resutado: ", self.resta
    
    def division(self):
        self.division = self.num1 / self.num2
        return"La division da como resultado: ", self.division

    def multiplicacion(self):
        self.multiplicacion = self.num1 * self.num2
        return"La multiplicacion da como resultado: " , self.multiplicacion
    
calculadora = Calculadora()
print(calculadora.suma())
print(calculadora.resta())
print(calculadora.division())
print(calculadora.multiplicacion())


